import asyncio
import copy
from dataclasses import dataclass
import time
import traceback
import textwrap
import socket
import struct
import threading
from typing import TYPE_CHECKING, Any, List, Optional

import Utils
from CommonClient import (
    ClientCommandProcessor,
    CommonContext,
    get_base_parser,
    gui_enabled,
    logger,
    server_loop,
)
from NetUtils import ClientStatus, NetworkItem

from .items import wsr_items

if TYPE_CHECKING:
    import kvui

class AsyncUDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, client):
        self.client: AsyncWiiMemoryClient = client
    
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

class AsyncWiiMemoryClient:
    def __init__(self, wii_ip, port=51234):
        self.wii_ip = wii_ip
        self.port = port
        self.transport = None
        self.protocol = None
        self.established = False

        self.command_queue = asyncio.Queue()
        self.current_request: Optional[CommandRequest] = None
        self.queue_processor_task = None

    async def connect(self):
        """Establish connection to the Wii"""
        try:
            loop = asyncio.get_event_loop()
            logger.info(f"ip: {self.wii_ip}")
            logger.info(f"port: {self.port}")
            self.transport, self.protocol = await loop.create_datagram_endpoint(
                lambda: AsyncUDPProtocol(self),
                local_addr=("10.0.0.116", 51235), # try empty string for ip/port 
                remote_addr=(self.wii_ip, self.port)
            )
            sock = self.transport.get_extra_info('socket')
            self.my_ip = sock.getsockname()[0]
            self.my_port = sock.getsockname()[1]

            logger.info("trying to connect...")

            self.queue_processor_task = asyncio.create_task(self._process_command_queue())

            try:
                await self.establish_connections()
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
        """Handle incoming UDP response"""
        if self.current_request and not self.current_request.future.done():
            self.current_request.future.set_result(data)
            self.current_request = None
        else:
            print(f"Received unexpected response: {data}")

    async def establish_connections(self, timeout=1):
        """Try to send a packet with IP and Port to establish connection to Wii server"""
        command = b'\x00' + socket.inet_aton(self.my_ip) + struct.pack('>H', self.my_port)
        
        response = await self._send_command_queued(command, timeout)

        logger.info(response)
        
        if len(response) > 0:
            return True
        else:
            raise Exception(f"Establishing UDP connection failed")
        
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
                    print(f"Sending UDP packet to {self.wii_ip}:{self.port}: {request.command.hex()}")
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
        
    async def signal_dc(self, timeout=2) -> bytes:
        """Send a signal to the wii that the client lost connection"""
        command = struct.pack('>B', 0x05) # DISCONNECT - 0x05

        response = await self._send_command_queued(command, timeout)

        if len(response) > 0:
            return response
        else:
            raise Exception(f"Read failed at address")
        
    def close(self):
        """Close connection"""
        self.established = False
        if self.transport:
            self.transport.close()
            self.transport = None


    async def write_bytes(self, data, packet_type_id=0, timeout=2):
        if packet_type_id == 0:
            raise Exception(f"invalid packet type id with data: {data}")

        data_len = len(data)

        packet_size = data_len.to_bytes(4, byteorder="big")

        response = await self._send_command_queued(packet_size, timeout)

        if len(response) != 1:
            raise Exception(f"Write failed with data {data}")

        packet_type_id = packet_type_id.to_bytes(1, byteorder="big")

        command = packet_type_id + data

        logger.info(f"Command: {command} | Data Length: {data_len} | Data: {data.hex()}")

        response = await self._send_command_queued(command, timeout)

        if len(response) == 1:
            return True
        else:
            raise Exception(f"Write failed with data {data}")

class WSRCommandProcessor(ClientCommandProcessor):
    """
    Command processor for WSR client commands
    """

    def __init__(self, ctx: CommonContext):
        """
        Initialize the command processor with the provided context

        @param ctx: Contex for the client
        """
        super().__init__(ctx)


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
        self.wii_memory_client: AsyncWiiMemoryClient = None
        self.wii_ip: str = "10.0.0.116"
        self.socket = None
        self.client_socket = None

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        """
        Disconnect the client from the server and reset game state variables

        @param allow_autoreconnect: Allow the client to auto-reconnect to the server. Default is false
        """
        self.auth = None
        await super().disconnect(allow_autoreconnect)


    def start_wii_client(self, ip):
        """Initialize the async Wii client"""
        if self.wii_memory_client:
            self.wii_memory_client.close()
        self.wii_memory_client = AsyncWiiMemoryClient(ip)

    def close_wii_client(self):
        if self.wii_memory_client:
            if self.wii_memory_client.established:
                self.wii_memory_client.signal_dc()
            self.wii_memory_client.close()
            self.wii_memory_client = None

    def is_hooked(self):
        return self.wii_memory_client and self.wii_memory_client.established

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
        logger.info("Authenticating server...")
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        if not self.auth:
            if self.awaiting_rom:
                return
            self.awaiting_rom = True
            logger.info("Awaiting connection to the game to get player information.")
            return
        await self.send_connect()

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        """
        Handle incoming packages from the server.

        @param cmd: Command received from server
        @param args: Command arguments
        """
        if cmd == "Connected":
            # this is where death link will be set up
            self.slot_data = args.get("slot_data", None)
            self.last_rcvd_index = -1
        elif cmd == "RoomInfo":
            self.seed_name = args["seed_name"]
        elif cmd == "Print":
            pass
        elif cmd == "ReceivedItems":
            if args["index"] >= self.last_rcvd_index:
                self.last_rcvd_index = args["index"]
                for item in args["items"]:
                    self.items_rcvd.append(item, self.last_rcvd_index)
                    self.last_rcvd_index += 1
                self.items_rcvd.sort(key=lambda v: v[1])
        elif cmd == "Retrieved":
            pass
        elif cmd == "SetReply":
            pass

    async def give_items(self) -> None:
        """
        Gives player all outstanding items they have not yet received
        
        @param self: The WSR client context
        """
        if await self.can_receive_items():
            for item in self.items_rcvd:
                await self._give_item(item)
        
        await self._give_item("Bowling (Standard) - Moving")

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

        logger.info(f"item id: {item_id}")

        item_id_byte: bytes = item_id.to_bytes(2, byteorder="big")

        logger.info(f"item id in bytes: {item_id_byte}")
        
        if await self.wii_memory_client.write_bytes(item_id_byte, packet_type_id=1):
            logger.info("sent item")
            return True
        
        logger.info("failed to send item")
        return False



    async def can_receive_items(self) -> bool:
        return True





async def do_sync_task(ctx: WSRContext) -> None:
    """
    Manages the connection to the game

    @param ctx: The WSR client context.
    """
    while not ctx.exit_event.is_set():
        try:
            if ctx.is_hooked():
                await ctx.give_items()
                #await ctx.check_locations()
                if ctx.awaiting_rom:
                    await ctx.server_auth()
                await asyncio.sleep(0.1)
            else:
                logger.info("Attempting to connect to the console...")
                ctx.close_wii_client()
                ctx.start_wii_client(ctx.wii_ip)
                await ctx.wii_memory_client.connect()

                if ctx.wii_memory_client.established:
                    logger.info("Wii connected successfully")
                    ctx.locations_checked = set()
                else:
                    logger.info(
                        "Connection to console failed, attempting again..."
                    )
                    await ctx.disconnect()
                    await asyncio.sleep(5)
                    continue
        except TimeoutError:
            print("Lost packet from console, attempting to reconnect...")
            ctx.close_wii_client()
            ctx.start_wii_client(ctx.wii_ip)
            if not await ctx.wii_memory_client.connect():
                logger.info(
                "Lost packet from console and couldn't reconnect. attempting to reconnect..."
                )
                await ctx.disconnect()
                await asyncio.sleep(5)
            else:
                print("Reconnected to console successfully!")
            continue
        except Exception:
            ctx.close_wii_client()
            logger.info(
                "Connection to console failed, attempting to reconnect..."
            )
            logger.error(traceback.format_exc())
            await ctx.disconnect()
            await asyncio.sleep(5)
            continue

def main(connect: Optional[str] = None, password: Optional[str] = None) -> None:
    """
    Run the main async loop for the WSR client.

    @param connect: Address of the AP server
    @param password: Password for server aunthentication
    """
    Utils.init_logging("Wii Sports Resort Client")

    async def _main(connect: Optional[str], Password: Optional[str]) -> None:
        ctx = WSRContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.sync_task = asyncio.create_task(
            do_sync_task(ctx), name="GameSync"
        )

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.sync_task:
            await asyncio.sleep(3)
            await ctx.sync_task

    import colorama

    colorama.just_fix_windows_console()
    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()

if __name__ == "__main__":
    parser = get_base_parser()
    args = parser.parse_args()
    main(args.connect, args.password)