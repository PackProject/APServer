from BaseClasses import Item
from BaseClasses import ItemClassification as ItemType
from typing import List, Dict, TYPE_CHECKING, Optional
from .types import WSRItemData, CategoryIndex, SportIndex
from .locations import get_total_locations

if TYPE_CHECKING:
    from . import WSRWorld

class WSRItem(Item):
    game = "Wii Sports Resort"
    type: Optional[str]

    def __init__(
        self,
        name: str,
        player: int,
        data: WSRItemData,
    ) -> None:
        super().__init__(
            name,
            data.classification,
            WSRItem.get_apid(data.item_id),
            player
        )

        self.type = data.itemType
        self.item_id = data.item_id

    @staticmethod
    def get_apid(id: int) -> int:
        """
        Returns the AP ID for any item index
        
        @param id: item id to convert
        """
        base_id: int = 543000
        return base_id + id




def create_itempool(world: "WSRWorld") -> List[Item]:
    itempool: List[Item] = []

    for name in item_table.keys():
        item_type: ItemType = item_table.get(name).classification

        if item_type is ItemType.filler or item_type is ItemType.trap:
            continue

        if item_table[name].itemType == "Unlock Category" and world.options.sports_unlock_state == 1:
            continue

        if item_table[name].itemType == "Unlock Sport" and world.options.sports_unlock_state == 0:
            continue

        #TOOO: Starting Items

        itempool += create_multiple_items(world, name, item_frequencies.get(name, 1), item_type)

    itempool += create_junk_items(world, len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool))
    return itempool


def create_item(world: "WSRWorld", name: str) -> Item:
    data = item_table[name]
    return WSRItem(name, world.player, data)


def create_multiple_items(world: "WSRWorld", name: str, count: int = 1, \
                          item_type: ItemType = ItemType.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist.append(WSRItem(name, world.player, data))

    return itemlist

def create_junk_items(world: "WSRWorld", count: int) -> List[Item]:
    junkpool: List[Item] = []
    junklist: Dict[str, int] = {}
    it: ItemType

    for name in item_table.keys():
        it = item_table[name].classification
        if it == ItemType.filler:
            junklist[name] = junk_weights.get(name)

    for i in range(count):
        junkpool.append(world.create_item(world.random.choices(list(junklist.keys()), \
                                                               weights = list(junklist.values()), k=1)[0]))
        
    return junkpool
    

#
# Any item that prevents the player from earning a stamp should be classified
# as a progression item.
#

wsr_items: dict[str, WSRItemData] = {
    #Category Unlocks
    "Unlock Swordplay":      WSRItemData("Unlock Category", ItemType.progression, 1, 0, 0x0014),
    "Unlock Wakeboarding":   WSRItemData("Unlock Category", ItemType.progression, 2, 0, 0x0015),
    "Unlock Frisbee":        WSRItemData("Unlock Category", ItemType.progression, 3, 0, 0x0016),
    "Unlock Archery":        WSRItemData("Unlock Category", ItemType.progression, 4, 0, 0x0017),
    "Unlock Basketball":     WSRItemData("Unlock Category", ItemType.progression, 5, 0, 0x0018),
    "Unlock Table Tennis":   WSRItemData("Unlock Category", ItemType.progression, 6, 0, 0x0019),
    "Unlock Golf":           WSRItemData("Unlock Category", ItemType.progression, 7, 0, 0x001A),
    "Unlock Bowling":        WSRItemData("Unlock Category", ItemType.progression, 8, 0, 0x001B),
    "Unlock Power Cruising": WSRItemData("Unlock Category", ItemType.progression, 9, 0, 0x001C),
    "Unlock Canoeing":       WSRItemData("Unlock Category", ItemType.progression, 10, 0, 0x001D),
    "Unlock Cycling":        WSRItemData("Unlock Category", ItemType.progression, 11, 0, 0x001E),
    "Unlock Air Sports":     WSRItemData("Unlock Category", ItemType.progression, 12, 0, 0x001F),

    #Sport Unlocks
    "Unlock Swordplay - Duel":                WSRItemData("Unlock Sport", ItemType.progression, 1, 1, 0x0000),
    "Unlock Swordplay - Speed Slice":         WSRItemData("Unlock Sport", ItemType.progression, 1, 2, 0x0001),
    "Unlock Swordplay - Showdown":            WSRItemData("Unlock Sport", ItemType.progression, 1, 3, 0x0002),
    "Unlock Wakeboarding":                    WSRItemData("Unlock Sport", ItemType.progression, 2, 4, 0x0015),
    "Unlock Frisbee - Frisbee Dog":           WSRItemData("Unlock Sport", ItemType.progression, 3, 5, 0x0004),
    "Unlock Frisbee - Frisbee Golf":          WSRItemData("Unlock Sport", ItemType.progression, 3, 6, 0x0005),
    "Unlock Archery":                         WSRItemData("Unlock Sport", ItemType.progression, 4, 7, 0x0017),
    "Unlock Basketball - 3 Point Contest":    WSRItemData("Unlock Sport", ItemType.progression, 5, 8, 0x0007),
    "Unlock Basketball - Pickup Game":        WSRItemData("Unlock Sport", ItemType.progression, 5, 9, 0x0008),
    "Unlock Table Tennis - Return Challenge": WSRItemData("Unlock Sport", ItemType.progression, 6, 10, 0x000A),
    "Unlock Table Tennis - Match":            WSRItemData("Unlock Sport", ItemType.progression, 6, 11, 0x0009),
    "Unlock Golf":                            WSRItemData("Unlock Sport", ItemType.progression, 7, 12, 0x001A),
    "Unlock Bowling - 10 Pin Game":           WSRItemData("Unlock Sport", ItemType.progression, 8, 13, 0x000C),
    "Unlock Bowling - 100 Pin Game":          WSRItemData("Unlock Sport", ItemType.progression, 8, 14, 0x000D),
    "Unlock Bowling - Spin Control":          WSRItemData("Unlock Sport", ItemType.progression, 8, 15, 0x000E),
    "Unlock Power Cruising":                  WSRItemData("Unlock Sport", ItemType.progression, 9, 16, 0x001C),
    "Unlock Canoeing":                        WSRItemData("Unlock Sport", ItemType.progression, 10, 17, 0x001D),
    "Unlock Cycling":                         WSRItemData("Unlock Sport", ItemType.progression, 11, 18, 0x001E),
    "Unlock Air Sports - Skydiving":          WSRItemData("Unlock Sport", ItemType.progression, 12, 19, 0x0012),
    "Unlock Air Sports - Island Flyover":     WSRItemData("Unlock Sport", ItemType.progression, 12, 20, 0x0013),

    #Level Unlocks
    "Unlock Swordplay Showdown - Bridge":             WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0302),
    "Unlock Swordplay Showdown - Lighthouse":         WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0303),
    "Unlock Swordplay Showdown - Beach":              WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0304),
    "Unlock Swordplay Showdown - Mountain":           WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0305),
    "Unlock Swordplay Showdown - Forest":             WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0306),
    "Unlock Swordplay Showdown - Ruins":              WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0307),
    "Unlock Swordplay Showdown - Waterfall":          WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0308),
    "Unlock Swordplay Showdown - Cliffs":             WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0309),
    "Unlock Swordplay Showdown - Castle":             WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x030A),
    "Unlock Swordplay Showdown - Volcano":            WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x030B),
    "Unlock Swordplay Showdown - Bridge Reverse":     WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x030C),
    "Unlock Swordplay Showdown - Lighthouse Reverse": WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x030D),
    "Unlock Swordplay Showdown - Beach Reverse":      WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x030E),
    "Unlock Swordplay Showdown - Mountain Reverse":   WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x030F),
    "Unlock Swordplay Showdown - Forest Reverse":     WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0310),
    "Unlock Swordplay Showdown - Ruins Reverse":      WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0311),
    "Unlock Swordplay Showdown - Waterfall Reverse":  WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0312),
    "Unlock Swordplay Showdown - Cliffs Reverse":     WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0313),
    "Unlock Swordplay Showdown - Castle Reverse":     WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0314),
    "Unlock Swordplay Showdown - Volcano Reverse":    WSRItemData("Unlock Level", ItemType.progression, 1,3, 0x0315),
    "Unlock Wakeboarding - Beginner":                 WSRItemData("Unlock Level", ItemType.progression, 2,4, 0x0401),
    "Unlock Wakeboarding - Intermediate":             WSRItemData("Unlock Level", ItemType.progression, 2,4, 0x0402),
    "Unlock Wakeboarding - Expert":                   WSRItemData("Unlock Level", ItemType.progression, 2,4, 0x0403),
    "Unlock Frisbee Golf - Classic A":                WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x0608),
    "Unlock Frisbee Golf - Classic B":                WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x0609),
    "Unlock Frisbee Golf - Classic C":                WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x060A),
    "Unlock Frisbee Golf - Resort A":                 WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x0605),
    "Unlock Frisbee Golf - Resort B":                 WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x0606),
    "Unlock Frisbee Golf - Resort C":                 WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x0607),
    "Unlock Frisbee Golf - Special":                  WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x060B),
    "Unlock Frisbee Golf - Classic 9":                WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x060D),
    "Unlock Frisbee Golf - Resort 9":                 WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x060C),
    "Unlock Frisbee Golf - 18 Hole":                  WSRItemData("Unlock Level", ItemType.progression, 3,6, 0x060E),
    "Unlock Archery - Beginner":                      WSRItemData("Unlock Level", ItemType.progression, 4,7, 0x705),
    "Unlock Archery - Intermediate":                  WSRItemData("Unlock Level", ItemType.progression, 4,7, 0x706),
    "Unlock Archery - Expert":                        WSRItemData("Unlock Level", ItemType.progression, 4,7, 0x707),
    "Unlock Golf - Classic A":                        WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B0F),
    "Unlock Golf - Classic B":                        WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B10),
    "Unlock Golf - Classic C":                        WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B11),
    "Unlock Golf - Resort A":                         WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B0C),
    "Unlock Golf - Resort B":                         WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B0D),
    "Unlock Golf - Resort C":                         WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B0E),
    "Unlock Golf - Special":                          WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B12),
    "Unlock Golf - Classic 9":                        WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B14),
    "Unlock Golf - Resort 9":                         WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B13),
    "Unlock Golf - 18 Hole":                          WSRItemData("Unlock Level", ItemType.progression, 7,12, 0x0B15),
    "Unlock Power Cruising - Beach":                  WSRItemData("Unlock Level", ItemType.progression, 9,16, 0x0F04),
    "Unlock Power Cruising - Lagoon":                 WSRItemData("Unlock Level", ItemType.progression, 9,16, 0x0F05),
    "Unlock Power Cruising - Lighthouse":             WSRItemData("Unlock Level", ItemType.progression, 9,16, 0x0F06),
    "Unlock Power Cruising - Marina":                 WSRItemData("Unlock Level", ItemType.progression, 9,16, 0x0F07),
    "Unlock Power Cruising - Cavern":                 WSRItemData("Unlock Level", ItemType.progression, 9,16, 0x0F08),
    "Unlock Power Cruising - Shoals":                 WSRItemData("Unlock Level", ItemType.progression, 9,16, 0x0F09),
    "Unlock Cycling - Around The Island":             WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1101),
    "Unlock Cycling - To The Beach":                  WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1102),
    "Unlock Cycling - Across The Bridge":             WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1103),
    "Unlock Cycling - Over Talon Rock":               WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1104),
    "Unlock Cycling - Up The Volcano":                WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1105),
    "Unlock Cycling - Into Maka Wuhu":                WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1106),
    "Unlock Cycling - 3-Stage Race A":                WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1107),
    "Unlock Cycling - 3-Stage Race B":                WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1108),
    "Unlock Cycling - 6 Stage":                       WSRItemData("Unlock Level", ItemType.progression, 11,18, 0x1109),
    "Unlock Island Flyover - Daytime":                WSRItemData("Unlock Level", ItemType.progression, 12,20, 0x1301),
    "Unlock Island Flyover - Evening":                WSRItemData("Unlock Level", ItemType.progression, 12,20, 0x1302),
    "Unlock Island Flyover - Night":                  WSRItemData("Unlock Level", ItemType.progression, 12,20, 0x1303),

    #Sport Timers
    "Wakeboarding Timer":                      WSRItemData("Timer", ItemType.progression_skip_balancing, 2,4, 0x0400),
    "Basketball (3-Point Contest) Timer":      WSRItemData("Timer", ItemType.progression_skip_balancing, 5,8, 0x0800),
    "Basketball (Pickup) Timer":               WSRItemData("Timer", ItemType.progression_skip_balancing, 5,9, 0x0900),
    "Power Cruising - Free Cruising Timer":    WSRItemData("Timer", ItemType.progression_skip_balancing, 9,16, 0x0F03),
    "Canoeing Timer":                          WSRItemData("Timer", ItemType.progression_skip_balancing, 10,17, 0x1000),
    "Island Flyover Timer":                    WSRItemData("Timer", ItemType.progression_skip_balancing, 12,20, 0x1300),

    #Extra Progression Items
    "Progressive Frisbee (Frisbee Dog)":           WSRItemData("Progression", ItemType.progression, 3,5, 0x0500),
    "Progressive Frisbee (Frisbee Golf)":          WSRItemData("Progression", ItemType.progression, 3,6, 0x0601),
    "Progressive Arrow (Archery)":                 WSRItemData("Progression", ItemType.progression, 4,7, 0x0701),
    "Progressive Fruit (Archery)":                 WSRItemData("Progression", ItemType.progression, 4,7, 0x702),
    "Basketball (3-Point Contest) - Golden Balls": WSRItemData("Progression", ItemType.progression, 5,8, 0x0801),
    "Basketball Pickup Game - Dunk":               WSRItemData("Progression", ItemType.progression, 5,9, 0x0903),
    "Table Tennis (Return Challenge) - Cans":      WSRItemData("Progression", ItemType.progression, 6,10, 0x0A02),
    "Progressive Club (Golf)":                     WSRItemData("Progression", ItemType.progression, 7,12, 0x0B01),
    "Golf - Turn":                                 WSRItemData("Progression", ItemType.progression, 7,12, 0x0B0A),
    "Bowling (Standard) - Turning":                WSRItemData("Progression", ItemType.progression, 8,13, 0x0C01),
    "Bowling (Standard) - Moving":                 WSRItemData("Progression", ItemType.progression, 8,13, 0x0C00),
    "Bowling (Standard) - Spin":                   WSRItemData("Progression", ItemType.progression, 8,13, 0x0C02),
    "Bowling (100 Pin) - Turning":                 WSRItemData("Progression", ItemType.progression, 8,14, 0x0D01),
    "Bowling (100 Pin) - Moving":                  WSRItemData("Progression", ItemType.progression, 8,14, 0x0D00),
    "Bowling (100 Pin) - Spin":                    WSRItemData("Progression", ItemType.progression, 8,14, 0x0D02),
    "Bowling (Spin Control) - Turning":            WSRItemData("Progression", ItemType.progression, 8,15, 0x0E01),
    "Bowling (Spin Control) - Moving":             WSRItemData("Progression", ItemType.progression, 8,15, 0x0E00),
    "Bowling (Spin Control) - Spin":               WSRItemData("Progression", ItemType.progression, 8,15, 0x0E02),
    "Power Cruising - Boost":                      WSRItemData("Progression", ItemType.progression, 9,16, 0x0F00),
    "Power Cruising - Double Ring":                WSRItemData("Progression", ItemType.progression, 9,16, 0x0F02),
    "Power Cruising - Progressive Ring Timer":     WSRItemData("Progression", ItemType.progression, 9,16, 0x0F01),
    "Cycling - Progressive Heart":                 WSRItemData("Progression", ItemType.progression, 11,18, 0x1100),
    "Cycling - Drafting":                          WSRItemData("Progression", ItemType.progression, 11,18, 0x110A),
    "Island Flyover - Double Blasters":            WSRItemData("Progression", ItemType.progression, 12,19, 0x1304),
    "Island Flyover - Night Lights":               WSRItemData("Progression", ItemType.progression, 12,19, 0x1305),
    "Island Flyover - Unlock Balloons":            WSRItemData("Progression", ItemType.progression, 12,19, 0x1306),
    "Island Flyover - Unlock Two Seater":          WSRItemData("Progression", ItemType.progression, 12,19, 0x1307),
    "Island Flyover - Unlock Boosting":            WSRItemData("Progression", ItemType.progression, 12,19, 0x1308),
    "Island Flyover - Unlock Braking":             WSRItemData("Progression", ItemType.progression, 12,19, 0x1309),
    "Skydiving - Mii":                             WSRItemData("Progression", ItemType.progression, 12,20, 0x1200),

    #Useful Items
    "Skydiving - Mii":                     WSRItemData("Progression", ItemType.progression, 12,20, 0x1200),
    "Swordplay Duel - Blocking":           WSRItemData("Useful", ItemType.useful, 1,1, 0x0100),
    "Swordplay Speed Slice - Pausing":     WSRItemData("Useful", ItemType.useful, 1,2, 0x0200),
    "Swordplay Showdown - Blocking":       WSRItemData("Useful", ItemType.useful, 1,3, 0x0300),
    "Swordplay - Progressive Heart":       WSRItemData("Useful", ItemType.useful, 1,3, 0x0301),
    "Frisbee Dog - A+2 Balloon Pop":       WSRItemData("Useful", ItemType.useful, 3,6, 0x0504),
    "Frisbee Golf - HUD":                  WSRItemData("Useful", ItemType.useful, 3,6, 0x0600),
    "Archery - Aiming Circle":             WSRItemData("Useful", ItemType.useful, 4,7, 0x0700),
    "Basketball Pickup Game - Passing":    WSRItemData("Useful", ItemType.useful, 5,9, 0x0901),
    "Basketball Pickup Game - 3-Pointers": WSRItemData("Useful", ItemType.useful, 5,9, 0x0902),
    "Table Tennis - Spin":                 WSRItemData("Useful", ItemType.useful, 6,11, 0x0A00),
    "Table Tennis - Smash Hit":            WSRItemData("Useful", ItemType.useful, 6,11, 0x0A01),
    "Golf - HUD":                          WSRItemData("Useful", ItemType.useful, 7,12, 0x0B00),
    "Golf - Backspin":                     WSRItemData("Useful", ItemType.useful, 7,12, 0x0B0B),
    "Golf - Green Low View":               WSRItemData("Useful", ItemType.useful, 7,12, 0x0B16),
    "Golf - Green Slope View":             WSRItemData("Useful", ItemType.useful, 7,12, 0x0B17),

    #Garbage Items
    "100 Skill Points (Swordplay Duel)":                  WSRItemData("Filler", ItemType.filler, 0,0, 0xFF00),
    "100 Skill Points (Swordplay Speed Slice)":           WSRItemData("Filler", ItemType.filler, 0,0, 0xFF01),
    "100 Skill Points (Swordplay Showdown)":              WSRItemData("Filler", ItemType.filler, 0,0, 0xFF02),
    "100 Skill Points (Wakeboarding)":                    WSRItemData("Filler", ItemType.filler, 0,0, 0xFF03),
    "100 Skill Points (Frisbee Dog)":                     WSRItemData("Filler", ItemType.filler, 0,0, 0xFF04),
    "100 Skill Points (Frisbee Golf)":                    WSRItemData("Filler", ItemType.filler, 0,0, 0xFF05),
    "100 Skill Points (Archery)":                         WSRItemData("Filler", ItemType.filler, 0,0, 0xFF06),
    "100 Skill Points (Basketball - 3 Point Contest)":    WSRItemData("Filler", ItemType.filler, 0,0, 0xFF07),
    "100 Skill Points (Basketball - Pickup Game)":        WSRItemData("Filler", ItemType.filler, 0,0, 0xFF08),
    "100 Skill Points (Table Tennis - Return Challenge)": WSRItemData("Filler", ItemType.filler, 0,0, 0xFF09),
    "100 Skill Points (Table Tennis - Match)":            WSRItemData("Filler", ItemType.filler, 0,0, 0xFF0A),
    "100 Skill Points (Golf)":                            WSRItemData("Filler", ItemType.filler, 0,0, 0xFF0B),
    "100 Skill Points (Bowling - 10-pin Game)":           WSRItemData("Filler", ItemType.filler, 0,0, 0xFF0C),
    "100 Skill Points (Bowling - 100-pin Game)":          WSRItemData("Filler", ItemType.filler, 0,0, 0xFF0D),
    "100 Skill Points (Bowling - Spin Control)":          WSRItemData("Filler", ItemType.filler, 0,0, 0xFF0E),
    "100 Skill Points (Power Cruising)":                  WSRItemData("Filler", ItemType.filler, 0,0, 0xFF0F),
    "100 Skill Points (Canoeing)":                        WSRItemData("Filler", ItemType.filler, 0,0, 0xFF10),
    "100 Skill Points (Cycling)":                         WSRItemData("Filler", ItemType.filler, 0,0, 0xFF11),
    "100 Skill Points (Air Sports - Skydiving)":          WSRItemData("Filler", ItemType.filler, 0,0, 0xFF12),
    "Extra Max Heart (Swordplay Showdown)":               WSRItemData("Filler", ItemType.filler, 0,0, 0xFF13),
    "Extra Max Heart (Cycling)":                          WSRItemData("Filler", ItemType.filler, 0,0, 0xFF14),
    "Random Cosmetic":                                    WSRItemData("Filler", ItemType.filler, 0,0, 0xFF15),
}

item_frequencies = {
    "Wakeboard Timer": 4,
    "Basketball (3PC) Timer": 4,
    "Basketball (Pickup) Timer": 4,
    "Power Cruising Timer": 5,
    "Canoeing Timer": 5,
    "Island Flyover Timer": 5,
    "Progressive Frisbee (Frisbee Dog)": 10,
    "Progressive Frisbee (Frisbee Golf)": 3,
    "Progressive Arrow (Archery)": 3,
    "Progressive Fruit (Archery)": 3,
    "Basketball (3-Point Contest) - Golden Balls": 5,
    "Progressive Club (Golf)": 8,
    "Progressive Ring Timer - Power Cruising": 2,
    "Progressive Heart - Cycling": 3,
    "Progressive Hearts - Swordplay": 3
}

junk_weights = {
    "100 Skill Points (Swordplay Duel)": 3,
    "100 Skill Points (Swordplay Speed Slice)": 3,
    "100 Skill Points (Swordplay Showdown)": 3,
    "100 Skill Points (Wakeboarding)": 3,
    "100 Skill Points (Frisbee Dog)": 3,
    "100 Skill Points (Frisbee Golf)": 3,
    "100 Skill Points (Archery)": 3,
    "100 Skill Points (Basketball - 3 Point Contest)": 3,
    "100 Skill Points (Basketball - Pickup Game)": 3,
    "100 Skill Points (Table Tennis - Return Challenge)": 3,
    "100 Skill Points (Table Tennis - Match)": 3,
    "100 Skill Points (Golf)": 3,
    "100 Skill Points (Bowling - 10-pin Game)": 3,
    "100 Skill Points (Bowling - 100-pin Game)": 3,
    "100 Skill Points (Bowling - Spin Control)": 3,
    "100 Skill Points (Power Cruising)": 3,
    "100 Skill Points (Canoeing)": 3,
    "100 Skill Points (Cycling)": 3,
    "100 Skill Points (Air Sports - Skydiving)": 3,
    "Extra Max Heart (Swordplay Showdown)": 3,
    "Extra Max Heart (Cycling)": 3,
    "Random Cosmetic": 42
}


item_table = {
    **wsr_items
}