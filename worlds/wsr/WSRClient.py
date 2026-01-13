import asyncio
import copy
from dataclasses import dataclass
import time
import traceback
import textwrap
import socket
import struct
import threading
from enum import IntEnum, auto
from typing import TYPE_CHECKING, Any, List, Optional
import colorama
from random import randint

import Utils
from CommonClient import (
    ClientCommandProcessor,
    CommonContext,
    get_base_parser,
    gui_enabled,
    logger,
    server_loop,
    mark_raw
)
from NetUtils import ClientStatus, NetworkItem, NetworkPlayer

from .items import wsr_items

if TYPE_CHECKING:
    import kvui

# =============================================================================#
# Constants                                                                    #
# =============================================================================#

# Whether to enable debugging features
DEBUG_MODE = True

# Port used by the Wii client
WII_PORT = 51234

# Port used by this PC client
CLIENT_PORT = 51235


class CommandID(IntEnum):
    """
    IDs for all PC -> Wii commands.
    """
    # default command id
    NONE = -1

    # PC client is attempting to connect
    CONNECT = 0
    
    # PC client is disconnecting
    DISCONNECT = auto()

    # PC client wants to display a message
    PRINT = auto()

    # PC client is sending an item
    ITEM = auto()

    # PC client is sending a request for location data
    LOCATION = auto()

# =============================================================================#
# AsyncUDPProtocol                                                             #
# =============================================================================#

class AsyncUDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, client):
        self.client: WiiClient = client
    
    def datagram_received(self, data, addr):
        print(f"Received UDP from {addr}: {data.hex()}")
        self.client.handle_response(data)

    def error_received(self, exc):
        print(f"UDP error: {exc}")
        self.client.established = False


class CommandRequest:
    def __init__(self, command: bytes, timeout: float = 10.0):
        self.command = command
        self.timeout = timeout
        self.future = asyncio.get_running_loop().create_future() # asyncio.Future()
        self.timestamp = time.time()

# =============================================================================#
# Wii client connection                                                        #
# =============================================================================#

class WiiClient:
    """
    Manages the connection with the Wii client.
    """
    
    def __init__(self, wii_ip, port=WII_PORT):
        self.wii_ip = wii_ip
        self.port = port
        self.transport = None
        self.protocol = None
        self.established = False

        self.command_queue = asyncio.Queue()
        self.current_request: Optional[CommandRequest] = None
        self.queue_processor_task = None

        self.most_recent_packet_data = []


    async def connect(self):
        """
        Establish connection to the Wii
        """

        try:
            loop = asyncio.get_event_loop()
            self.transport, self.protocol = await loop.create_datagram_endpoint(
                lambda: AsyncUDPProtocol(self),
                local_addr=("0.0.0.0", CLIENT_PORT),
                remote_addr=(self.wii_ip, self.port)
            )
            sock = self.transport.get_extra_info('socket')
            self.my_ip = sock.getsockname()[0]
            self.my_port = sock.getsockname()[1]

            self.queue_processor_task = asyncio.create_task(self._process_command_queue())

            try:
                await self.send_connect_cmd()
                self.established = True
                return True
            except asyncio.TimeoutError:
                self.established = False
                return False

        except Exception as e:
            print(f"Connection failed: {e}")
            self.established = False
            return False


    async def disconnect(self):
        if self.queue_processor_task:
            self.queue_processor_task.cancel()

            try:
                await self.queue_processor_task
            except asyncio.CancelledError:
                pass
            
        if self.transport:
            self.transport.close()

        self.established = False


    def handle_response(self, data):
        """
        Handle incoming UDP response
        """
        self.most_recent_packet_data = data

        if self.current_request and not self.current_request.future.done():
            self.current_request.future.set_result(data)
            self.current_request = None
        else:
            print(f"Received unexpected response: {data}")


    async def send_connect_cmd(self, timeout=1):
        """
        Try to send a packet with IP and Port to establish connection to Wii server
        """

        # Tell the wii who to return packets to
        packet = socket.inet_aton(self.my_ip) + struct.pack('>H', self.my_port)
        await self.send_packet(packet, CommandID.CONNECT)


    async def send_disconnect_cmd(self, timeout=2):
        """
        Send a signal to the wii that the client lost connection
        """

        # Disconnect command has no additional data
        await self.send_packet(bytes(), CommandID.DISCONNECT)
        

    async def send_print_cmd(self, args: dict[str, Any], timeout=2):
        """
        Send a message to the Wii to display
        """

        # Wii will expect UTF-16 encoded messages
        packet = args["data"].encode("utf-16-be")
        packet += bytearray(2) # null terminator

        await self.send_packet(packet, CommandID.PRINT)


    async def _send_command_queued(self, command: bytes, timeout=2):
        """Queue up command to read/write to console"""

        request = CommandRequest(command, timeout)
        await self.command_queue.put(request)

        try:
            response = await asyncio.wait_for(request.future, timeout=timeout)
            return response
        except asyncio.TimeoutError:
            print(f"Command {command} timed out")
            self.established = False
            raise


    async def _process_command_queue(self):
        """Process commands from queue with rate limiting"""

        while True:
            try:
                request = await self.command_queue.get()

                if self.transport and not request.future.cancelled():
                    self.current_request = request
                    self.transport.sendto(request.command)

                    asyncio.create_task(self._handle_request_timeout(request))
                elif request.future and not request.future.cancelled():
                    request.future.set_exception(ConnectionError("Not connected"))
            
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"Error in command queue: {e}")
                if self.current_request and not self.current_request.future.cancelled():
                    self.current_request.future.set_exception(e)


    async def _handle_request_timeout(self, request: CommandRequest):
        """Handle tieout for a specific request"""

        try:
            await asyncio.sleep(request.timeout)
            if self.current_request == request and not request.future.done():
                request.future.set_exception(asyncio.TimeoutError())
                self.current_request = None
        except asyncio.CancelledError:
            pass


    def close(self):
        """Close connection"""

        self.established = False

        if self.transport:
            self.transport.close()
            self.transport = None


    async def send_packet(self, data, packet_type_id=CommandID.NONE, timeout=2):
        """Send a single packet to the wii client"""

        packet = bytearray()
        packet += struct.pack(">B", packet_type_id) # id: u8 
        packet += data                              # data: byte[]

        if len(packet) > 512:
            raise Exception("Cannot send more than 512 bytes per packet")

        print(f"[send_packet] id={packet_type_id}, data={data}")

        # expect 0xAA byte for ack
        response = await self._send_command_queued(packet, timeout)
        if (len(response) == 1 and response[0] == 0xAA) or (packet_type_id == CommandID.LOCATION and len(response) > 0):
            return True
        
        raise Exception(f"Packet went unacknowledged: {packet}")

# =============================================================================#
# Command processor                                                            #
# =============================================================================#

class WSRCommandProcessor(ClientCommandProcessor):
    """
    Command processor for WSR client commands.
    """

    def __init__(self, ctx: CommonContext):
        """
        Initialize the command processor with the provided context

        @param ctx: Context for the client
        """

        super().__init__(ctx)


    def _cmd_wii_connect(self, wii_ip: str = -1) -> None:
        """
        Configures the IP address of the Wii console.

        @param wii_ip: IP address to use when communicating with the Wii
        """

        if wii_ip == -1:
            logger.info("Please enter a valid IP")
            return

        assert isinstance(self.ctx, WSRContext)

        # Terminate any existing connection
        Utils.async_start(self.ctx.disconnect())

        self.ctx.wii_ip = wii_ip

    @mark_raw
    def _cmd_debug_item(self, item_name = "") -> None:
        """
        Send an item command for debugging purposes.
        If no item is specified, a random item is chosen.

        @param item_name: Specified item name (optional)
        """

        assert isinstance(self.ctx, WSRContext)

        if not DEBUG_MODE:
            return

        # Defaults to a random item
        if not item_name:
            item_name = "Bowling (Standard) - Moving"

        Utils.async_start(self.ctx._give_item(item_name))


    @mark_raw
    def _cmd_debug_print(self, msg = "dummy") -> None:
        """
        Send a printcommand for debugging purposes.

        @param msg: Message text
        """

        assert isinstance(self.ctx, WSRContext)

        if not DEBUG_MODE:
            return

        # Mock PrintJSON command
        args = {"data": msg}

        Utils.async_start(self.ctx.wii_client.send_print_cmd(args))

    def _cmd_check_locations(self, msg = "dummy") -> None:
        """
        Send a check location command for debugging purposes.
        
        @param self: WSRCommandProcessor
        @param msg: does nothing
        """
        if not isinstance(self.ctx, WSRContext):
            logger.info("Please connect to the wii first")

        if not DEBUG_MODE:
            return

        Utils.async_start(self.ctx.check_locations())

# =============================================================================#
# Game context                                                                 #
# =============================================================================#

class WSRContext(CommonContext):
    """
    The context for the WSR client.

    Manages the connection between the server and the console.
    """

    command_processor = WSRCommandProcessor
    game: str = "Wii Sports Resort"

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        """
        Initialize the WSR context.

        @param server_address: Address of the AP server.
        @param password: Password for server aunthentication.
        """
        
        super().__init__(server_address, password)

        self.items_rcvd: list[tuple[NetworkItem, int]] = []
        self.sync_task: Optional[asyncio.Task[None]] = None
        self.last_rcvd_index = -1
        self.awaiting_rom: bool = False
        self.wii_client: WiiClient = None
        self.wii_ip: str = ""
        self.socket = None
        self.client_socket = None


    def log(self, msg: str, color: str = "white"):
        """
        Logs a message to the Archipelago UI, in the specified color.

        @param msg: Message text
        @param color: Text color name (defaults to "white")
        """

        print(msg)
        self.ui.print_json([{"text": msg, "type": "color", "color": color}])


    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        """
        Disconnect the client from the server and reset game state variables

        @param allow_autoreconnect: Allow the client to auto-reconnect to the server. Default is false
        """
        self.auth = None
        await super().disconnect(allow_autoreconnect)


    def start_wii_client(self, ip):
        """Initialize the async Wii client"""
        if self.wii_client:
            self.wii_client.close()

        self.wii_client = WiiClient(ip)


    def close_wii_client(self):
        if self.wii_client:
            if self.wii_client.established:
                self.wii_client.send_disconnect_cmd()

            self.wii_client.close()
            self.wii_client = None


    def is_hooked(self):
        return self.wii_client and self.wii_client.established


    def make_gui(self) -> type["kvui.GameManager"]:
        """
        Initialize the GUI for WSR Client.

        Returns the client's GUI.
        """
        ui = super().make_gui()
        ui.base_title = "Archipelago Wii Sports Resort Client"
        return ui


    async def server_auth(self, password_requested: bool = False) -> None:
        """
        Authenticate with the Archipelago server.

        @param password_requested: Whether the server requires a password. Defaults to `False`.
        """

        self.log("Authenticating with the Archipelago server...")

        if password_requested and not self.password:
            await super().server_auth(password_requested)

        if not self.auth:
            if not self.awaiting_rom:
                self.awaiting_rom = True
                self.log("Waiting to connect to the game for player information.")
        else:
            await self.send_connect()


    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        """
        Handle incoming packages from the server.

        @param cmd: Command received from server
        @param args: Command arguments
        """

        if cmd == "ReceivedItems":
            # Validate package by checking against the last known item index
            if args["index"] >= self.last_rcvd_index:
                self.last_rcvd_index = args["index"]

                for item in args["items"]:
                    self.items_rcvd.append(item, self.last_rcvd_index)
                    self.last_rcvd_index += 1
                
                self.items_rcvd.sort(key=lambda v: v[1])

        elif cmd == "LocationInfo":
            # TODO: I think we may want this
            pass

        elif cmd == "PrintJSON":
            self.wii_client.send_print_cmd(args)


    async def give_items(self) -> None:
        """
        Gives player all outstanding items they have not yet received
        
        @param self: The WSR client context
        """
        if await self.can_receive_items():
            for item in self.items_rcvd:
                await self._give_item(item)


    async def check_locations(self) -> None:
        """
        Iterate through all locations and check whether the player has checked each location.

        Update the server with all newly checked locations since the last update. If the player has completed the goal,
        notify the server.

        @param self: The WSR client context.
        """
        if not isinstance(self.wii_client, WiiClient):
            logger.info("Please connect to the wii first")
            return

        response = await self.wii_client.send_packet(bytes(), packet_type_id=CommandID.LOCATION)

        logger.info(f"Location Data in bytes: {self.wii_client.most_recent_packet_data}")
        


    async def _give_item(self, item_name: str) -> bool:
        """
        Give an item to the player.

        @param self: The WSR client context
        @param item_name: The name of the item
        @return: whether the process was successful
        """
        if not await self.can_receive_items():
            return False
        
        item_id = wsr_items[item_name].item_id

        self.log(f"item id: {item_id}")

        item_id_byte: bytes = item_id.to_bytes(2, byteorder="big")

        self.log(f"item id in bytes: {item_id_byte}")
        
        if await self.wii_client.send_packet(item_id_byte, packet_type_id=CommandID.ITEM):
            self.log("sent item")
            return True
        
        self.log("failed to send item")
        return False


    async def can_receive_items(self) -> bool:
        return True

# =============================================================================#
# Game sync coroutine                                                          #
# =============================================================================#

async def sync_loop(ctx: WSRContext) -> None:
    """
    The coroutine for managing the connection with the game.

    @param ctx: The WSR client context.
    """

    ctx.log("Use the /wii_connect command to connect to the console.", color="orange")

    # Sync loop will run until window close request
    while not ctx.exit_event.is_set():

        # User must provide the Wii's ip address
        if not ctx.wii_ip:
            await asyncio.sleep(5)
            continue
        
        try:
            if ctx.is_hooked():
                await ctx.give_items()
                await ctx.check_locations()
                
                if ctx.awaiting_rom:
                    await ctx.server_auth()
                
                await asyncio.sleep(0.1)
            else:
                ctx.log("Attempting to connect to the console...")

                ctx.close_wii_client()
                ctx.start_wii_client(ctx.wii_ip)

                if await ctx.wii_client.connect():
                    ctx.log("Wii connected successfully!")
                    ctx.locations_checked = set()
                else:
                    ctx.log("Connection to console failed.")
                    await ctx.disconnect()
                    await asyncio.sleep(5)

        # Console didn't acknowledge a packet in time, try to re-connect
        except TimeoutError:
            ctx.log("Timed out waiting for a response from the console.")
            await asyncio.sleep(5)

        # Generic exception, just reset the Wii client and try again
        except Exception:
            ctx.log("Failed to connect to the console.")
            ctx.log(traceback.format_exc(), color="red")
            await asyncio.sleep(5)

# =============================================================================#
# Main function                                                                #
# =============================================================================#

def main(connect: Optional[str] = None, password: Optional[str] = None) -> None:
    """
    Run the main async loop for the WSR client.

    @param connect: Address of the AP server
    @param password: Password for server aunthentication
    """

    Utils.init_logging("Wii Sports Resort Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        """
        Main coroutine for the WSR client.

        @param connect: Address of the AP server
        @param password: Password for server aunthentication
        """

        ctx = WSRContext(connect, password)

        # Create common server loop task
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        # Start client interface
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        # Begin trying to connect to the game
        await asyncio.sleep(1)
        ctx.sync_task = asyncio.create_task(sync_loop(ctx), name="GameSync")

        # Wait for window close request
        await ctx.exit_event.wait()

        # Terminate connection
        ctx.server_address = None
        await ctx.shutdown()

        # Wait for old sync task to finish
        if ctx.sync_task:
            await ctx.sync_task

    # Use colorama to display colored text
    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser()
    args = parser.parse_args()
    main(args.connect, args.password)