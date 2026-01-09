from BaseClasses import Item
from BaseClasses import ItemClassification as ItemType
from typing import List, Dict, TYPE_CHECKING
from .types import WSRItemData, WSRSport
from .locations import get_total_locations

if TYPE_CHECKING:
    from . import WSRWorld

#
# Writing data.sport instead of having data.code could cause issues.
# If there are issues with creating item pool, look there first
#


class WSRItem(Item):
    game = "Wii Sports Resort"


#
# Writing only progressive items at the moment, will update with non-progressive items later
#


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

    itempool += create_junk_items(world, get_total_locations(world) - len(itempool))
    return itempool


def create_item(world: "WSRWorld", name: str) -> Item:
    data = item_table[name]
    return WSRItem(name, data.classification, data.sport, world.player)


def create_multiple_items(world: "WSRWorld", name: str, count: int = 1, \
                          item_type: ItemType = ItemType.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [WSRItem(name, item_type, data.sport, world.player)]

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
    "Unlock Swordplay":      WSRItemData("Unlock Category", ItemType.progression, WSRSport(1, 0), 0),
    "Unlock Wakeboarding":   WSRItemData("Unlock Category", ItemType.progression, WSRSport(2, 0), 1),
    "Unlock Frisbee":        WSRItemData("Unlock Category", ItemType.progression, WSRSport(3, 0), 1),
    "Unlock Archery":        WSRItemData("Unlock Category", ItemType.progression, WSRSport(4, 0), 1),
    "Unlock Basketball":     WSRItemData("Unlock Category", ItemType.progression, WSRSport(5, 0), 1),
    "Unlock Table Tennis":   WSRItemData("Unlock Category", ItemType.progression, WSRSport(6, 0), 1),
    "Unlock Golf":           WSRItemData("Unlock Category", ItemType.progression, WSRSport(7, 0), 1),
    "Unlock Bowling":        WSRItemData("Unlock Category", ItemType.progression, WSRSport(8, 0), 1),
    "Unlock Power Cruising": WSRItemData("Unlock Category", ItemType.progression, WSRSport(9, 0), 1),
    "Unlock Canoeing":       WSRItemData("Unlock Category", ItemType.progression, WSRSport(10, 0), 1),
    "Unlock Cycling":        WSRItemData("Unlock Category", ItemType.progression, WSRSport(11, 0), 1),
    "Unlock Air Sports":     WSRItemData("Unlock Category", ItemType.progression, WSRSport(12, 0), 1),

    #Sport Unlocks
    "Unlock Swordplay - Duel":                WSRItemData("Unlock Sport", ItemType.progression, WSRSport(1, 1), 1),
    "Unlock Swordplay - Speed Slice":         WSRItemData("Unlock Sport", ItemType.progression, WSRSport(1, 2), 1),
    "Unlock Swordplay - Showdown":            WSRItemData("Unlock Sport", ItemType.progression, WSRSport(1, 3), 1),
    "Unlock Wakeboarding":                    WSRItemData("Unlock Sport", ItemType.progression, WSRSport(2, 4), 1),
    "Unlock Frisbee - Frisbee Dog":           WSRItemData("Unlock Sport", ItemType.progression, WSRSport(3, 5), 1),
    "Unlock Frisbee - Frisbee Golf":          WSRItemData("Unlock Sport", ItemType.progression, WSRSport(3, 6), 1),
    "Unlock Archery":                         WSRItemData("Unlock Sport", ItemType.progression, WSRSport(4, 7), 1),
    "Unlock Basketball - 3 Point Contest":    WSRItemData("Unlock Sport", ItemType.progression, WSRSport(5, 8), 1),
    "Unlock Basketball - Pickup Game":        WSRItemData("Unlock Sport", ItemType.progression, WSRSport(5, 9), 1),
    "Unlock Table Tennis - Return Challenge": WSRItemData("Unlock Sport", ItemType.progression, WSRSport(6, 10), 1),
    "Unlock Table Tennis - Match":            WSRItemData("Unlock Sport", ItemType.progression, WSRSport(6, 11), 1),
    "Unlock Golf":                            WSRItemData("Unlock Sport", ItemType.progression, WSRSport(7, 12), 1),
    "Unlock Bowling - 10 Pin Game":           WSRItemData("Unlock Sport", ItemType.progression, WSRSport(8, 13), 1),
    "Unlock Bowling - 100 Pin Game":          WSRItemData("Unlock Sport", ItemType.progression, WSRSport(8, 14), 1),
    "Unlock Bowling - Spin Control":          WSRItemData("Unlock Sport", ItemType.progression, WSRSport(8, 15), 1),
    "Unlock Power Cruising":                  WSRItemData("Unlock Sport", ItemType.progression, WSRSport(9, 16), 1),
    "Unlock Canoeing":                        WSRItemData("Unlock Sport", ItemType.progression, WSRSport(10, 17), 1),
    "Unlock Cycling":                         WSRItemData("Unlock Sport", ItemType.progression, WSRSport(11, 18), 1),
    "Unlock Air Sports - Skydiving":          WSRItemData("Unlock Sport", ItemType.progression, WSRSport(12, 19), 1),
    "Unlock Air Sports - Island Flyover":     WSRItemData("Unlock Sport", ItemType.progression, WSRSport(12, 20), 1),

    #Level Unlocks
    "Unlock Swordplay Showdown - Bridge":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Lighthouse":         WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Beach":              WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Mountain":           WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Forest":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Ruins":              WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Waterfall":          WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Cliffs":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Castle":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Volcano":            WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Bridge Reverse":     WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Lighthouse Reverse": WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Beach Reverse":      WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Mountain Reverse":   WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Forest Reverse":     WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Ruins Reverse":      WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Waterfall Reverse":  WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Cliffs Reverse":     WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Castle Reverse":     WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Swordplay Showdown - Volcano Reverse":    WSRItemData("Unlock Level", ItemType.progression, WSRSport(1,3), 1),
    "Unlock Wakeboarding - Beginner":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(2,4), 1),
    "Unlock Wakeboarding - Intermediate":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(2,4), 1),
    "Unlock Wakeboarding - Expert":                   WSRItemData("Unlock Level", ItemType.progression, WSRSport(2,4), 1),
    "Unlock Frisbee Golf - Classic A":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Classic B":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Classic C":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Resort A":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Resort B":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Resort C":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Special":                  WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Classic 9":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - Resort 9":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Frisbee Golf - 18 Hole":                  WSRItemData("Unlock Level", ItemType.progression, WSRSport(3,6), 1),
    "Unlock Archery - Beginner":                      WSRItemData("Unlock Level", ItemType.progression, WSRSport(4,7), 1),
    "Unlock Archery - Intermediate":                  WSRItemData("Unlock Level", ItemType.progression, WSRSport(4,7), 1),
    "Unlock Archery - Expert":                        WSRItemData("Unlock Level", ItemType.progression, WSRSport(4,7), 1),
    "Unlock Golf - Classic A":                        WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Classic B":                        WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Classic C":                        WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Resort A":                         WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Resort B":                         WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Resort C":                         WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Special":                          WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Classic 9":                        WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - Resort 9":                         WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Golf - 18 Hole":                          WSRItemData("Unlock Level", ItemType.progression, WSRSport(7,12), 1),
    "Unlock Power Cruising - Beach":                  WSRItemData("Unlock Level", ItemType.progression, WSRSport(9,16), 1),
    "Unlock Power Cruising - Lagoon":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(9,16), 1),
    "Unlock Power Cruising - Lighthouse":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(9,16), 1),
    "Unlock Power Cruising - Marina":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(9,16), 1),
    "Unlock Power Cruising - Cavern":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(9,16), 1),
    "Unlock Power Cruising - Shoals":                 WSRItemData("Unlock Level", ItemType.progression, WSRSport(9,16), 1),
    "Unlock Cycling - Around The Island":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - To The Beach":                  WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - Across The Bridge":             WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - Over Talon Rock":               WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - Up The Volcano":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - Into Maka Wuhu":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - 3-Stage Race A":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - 3-Stage Race B":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Cycling - 6 Stage":                       WSRItemData("Unlock Level", ItemType.progression, WSRSport(11,18), 1),
    "Unlock Island Flyover - Daytime":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(12,20), 1),
    "Unlock Island Flyover - Evening":                WSRItemData("Unlock Level", ItemType.progression, WSRSport(12,20), 1),
    "Unlock Island Flyover - Night":                  WSRItemData("Unlock Level", ItemType.progression, WSRSport(12,20), 1),

    #Sport Timers
    "Wakeboarding Timer":                      WSRItemData("Timer", ItemType.progression_skip_balancing, WSRSport(2,4), 1),
    "Basketball (3PC) Timer":                  WSRItemData("Timer", ItemType.progression_skip_balancing, WSRSport(5,8), 1),
    "Basketball (Pickup) Timer":               WSRItemData("Timer", ItemType.progression_skip_balancing, WSRSport(5,9), 1),
    "Power Cruising - Free Cruising Timer":      WSRItemData("Timer", ItemType.progression_skip_balancing, WSRSport(9,16), 1),
    "Canoeing Timer":                          WSRItemData("Timer", ItemType.progression_skip_balancing, WSRSport(10,17), 1),
    "Island Flyover Timer":                    WSRItemData("Timer", ItemType.progression_skip_balancing, WSRSport(12,20), 1),

    #Extra Progression Items
    "Progressive Frisbee (Frisbee Dog)":           WSRItemData("Progression", ItemType.progression, WSRSport(3,5), 1),
    "Progressive Frisbee (Frisbee Golf)":          WSRItemData("Progression", ItemType.progression, WSRSport(3,6), 1),
    "Progressive Arrow (Archery)":                 WSRItemData("Progression", ItemType.progression, WSRSport(4,7), 1),
    "Progressive Fruit (Archery)":                 WSRItemData("Progression", ItemType.progression, WSRSport(4,7), 1),
    "Basketball (3-Point Contest) - Golden Balls": WSRItemData("Progression", ItemType.progression, WSRSport(5,8), 1),
    "Basketball Pickup Game - Dunk":               WSRItemData("Progression", ItemType.progression, WSRSport(5,9), 1),
    "Table Tennis (Return Challenge) - Cans":      WSRItemData("Progression", ItemType.progression, WSRSport(6,7), 1),
    "Progressive Club (Golf)":                     WSRItemData("Progression", ItemType.progression, WSRSport(7,12), 1),
    "Golf - Turn":                                 WSRItemData("Progression", ItemType.progression, WSRSport(7,12), 1),
    "Bowling (Standard) - Turning":                WSRItemData("Progression", ItemType.progression, WSRSport(8,13), 1),
    "Bowling (Standard) - Moving":                 WSRItemData("Progression", ItemType.progression, WSRSport(8,13), 1),
    "Bowling (Standard) - Spin":                   WSRItemData("Progression", ItemType.progression, WSRSport(8,13), 1),
    "Bowling (100 Pin) - Turning":                 WSRItemData("Progression", ItemType.progression, WSRSport(8,14), 1),
    "Bowling (100 Pin) - Moving":                  WSRItemData("Progression", ItemType.progression, WSRSport(8,14), 1),
    "Bowling (100 Pin) - Spin":                    WSRItemData("Progression", ItemType.progression, WSRSport(8,14), 1),
    "Bowling (Spin Control) - Turning":            WSRItemData("Progression", ItemType.progression, WSRSport(8,15), 1),
    "Bowling (Spin Control) - Moving":             WSRItemData("Progression", ItemType.progression, WSRSport(8,15), 1),
    "Bowling (Spin Control) - Spin":               WSRItemData("Progression", ItemType.progression, WSRSport(8,15), 1),
    "Power Cruising - Boost":                      WSRItemData("Progression", ItemType.progression, WSRSport(9,16), 1),
    "Power Cruising - Double Ring":                WSRItemData("Progression", ItemType.progression, WSRSport(9,16), 1),
    "Power Cruising - Progressive Ring Timer":     WSRItemData("Progression", ItemType.progression, WSRSport(9,16), 1),
    "Cycling - Progressive Heart":                 WSRItemData("Progression", ItemType.progression, WSRSport(11,18), 1),
    "Cycling - Drafting":                          WSRItemData("Progression", ItemType.progression, WSRSport(11,18), 1),
    "Island Flyover - Double Blasters":            WSRItemData("Progression", ItemType.progression, WSRSport(12,19), 1),
    "Island Flyover - Night Lights":               WSRItemData("Progression", ItemType.progression, WSRSport(12,19), 1),
    "Island Flyover - Unlock Balloons":            WSRItemData("Progression", ItemType.progression, WSRSport(12,19), 1),
    "Island Flyover - Unlock Two Seater":          WSRItemData("Progression", ItemType.progression, WSRSport(12,19), 1),
    "Island Flyover - Unlock Boosting":            WSRItemData("Progression", ItemType.progression, WSRSport(12,19), 1),
    "Island Flyover - Unlock Braking":             WSRItemData("Progression", ItemType.progression, WSRSport(12,19), 1),
    "Skydiving - Mii":                             WSRItemData("Progression", ItemType.progression, WSRSport(12,20), 1),

    #Useful Items
    "Swordplay Duel - Blocking":           WSRItemData("Useful", ItemType.useful, WSRSport(1,1), 1),
    "Swordplay Speed Slice - Pausing":     WSRItemData("Useful", ItemType.useful, WSRSport(1,2), 1),
    "Swordplay Showdown - Blocking":       WSRItemData("Useful", ItemType.useful, WSRSport(1,3), 1),
    "Swordplay - Progressive Heart":      WSRItemData("Useful", ItemType.useful, WSRSport(1,3), 1),
    "Frisbee Dog - A+2 Balloon Pop":       WSRItemData("Useful", ItemType.useful, WSRSport(3,6), 1),
    "Frisbee Golf - HUD":                  WSRItemData("Useful", ItemType.useful, WSRSport(3,6), 1),
    "Archery - Aiming Circle":             WSRItemData("Useful", ItemType.useful, WSRSport(4,7), 1),
    "Basketball Pickup Game - Passing":    WSRItemData("Useful", ItemType.useful, WSRSport(5,9), 1),
    "Basketball Pickup Game - 3-Pointers": WSRItemData("Useful", ItemType.useful, WSRSport(5,9), 1),
    "Table Tennis - Spin":                 WSRItemData("Useful", ItemType.useful, WSRSport(6,11), 1),
    "Table Tennis - Smash Hit":            WSRItemData("Useful", ItemType.useful, WSRSport(6,11), 1),
    "Golf - HUD":                          WSRItemData("Useful", ItemType.useful, WSRSport(7,12), 1),
    "Golf - Backspin":                     WSRItemData("Useful", ItemType.useful, WSRSport(7,12), 1),
    "Golf - Green Low View":               WSRItemData("Useful", ItemType.useful, WSRSport(7,12), 1),
    "Golf - Green Slope View":             WSRItemData("Useful", ItemType.useful, WSRSport(7,12), 1),

    #Garbage Items
    "100 Skill Points (Swordplay Duel)":                  WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Swordplay Speed Slice)":           WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Swordplay Showdown)":              WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Wakeboarding)":                    WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Frisbee Dog)":                     WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Frisbee Golf)":                    WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Archery)":                         WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Basketball - 3 Point Contest)":    WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Basketball - Pickup Game)":        WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Table Tennis - Return Challenge)": WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Table Tennis - Match)":            WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Golf)":                            WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Bowling - 10-pin Game)":           WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Bowling - 100-pin Game)":          WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Bowling - Spin Control)":          WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Power Cruising)":                  WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Canoeing)":                        WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Cycling)":                         WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "100 Skill Points (Air Sports - Skydiving)":          WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "Extra Max Heart (Swordplay Showdown)":               WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "Extra Max Heart (Cycling)":                          WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
    "Random Cosmetic":                                    WSRItemData("Filler", ItemType.filler, WSRSport(0,0), 1),
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
    "Random Cosmetic": 37
}


item_table = {
    **wsr_items
}