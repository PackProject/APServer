from BaseClasses import Item
from BaseClasses import ItemClassification as ItemType
from typing import List, Dict, TYPE_CHECKING
from .types import ItemData, WSRSport
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

wsr_items = {
    #Category Unlocks
    "Unlock Swordplay":      ItemData("Unlock Category", ItemType.progression, WSRSport(1, 0)),
    "Unlock Wakeboarding":   ItemData("Unlock Category", ItemType.progression, WSRSport(2, 0)),
    "Unlock Frisbee":        ItemData("Unlock Category", ItemType.progression, WSRSport(3, 0)),
    "Unlock Archery":        ItemData("Unlock Category", ItemType.progression, WSRSport(4, 0)),
    "Unlock Basketball":     ItemData("Unlock Category", ItemType.progression, WSRSport(5, 0)),
    "Unlock Table Tennis":   ItemData("Unlock Category", ItemType.progression, WSRSport(6, 0)),
    "Unlock Golf":           ItemData("Unlock Category", ItemType.progression, WSRSport(7, 0)),
    "Unlock Bowling":        ItemData("Unlock Category", ItemType.progression, WSRSport(8, 0)),
    "Unlock Power Cruising": ItemData("Unlock Category", ItemType.progression, WSRSport(9, 0)),
    "Unlock Canoeing":       ItemData("Unlock Category", ItemType.progression, WSRSport(10, 0)),
    "Unlock Cycling":        ItemData("Unlock Category", ItemType.progression, WSRSport(11, 0)),
    "Unlock Air Sports":     ItemData("Unlock Category", ItemType.progression, WSRSport(12, 0)),

    #Sport Unlocks
    "Unlock Swordplay - Duel":                ItemData("Unlock Sport", ItemType.progression, WSRSport(1, 1)),
    "Unlock Swordplay - Speed Slice":         ItemData("Unlock Sport", ItemType.progression, WSRSport(1, 2)),
    "Unlock Swordplay - Showdown":            ItemData("Unlock Sport", ItemType.progression, WSRSport(1, 3)),
    "Unlock Wakeboarding":                    ItemData("Unlock Sport", ItemType.progression, WSRSport(2, 4)),
    "Unlock Frisbee - Frisbee Dog":           ItemData("Unlock Sport", ItemType.progression, WSRSport(3, 5)),
    "Unlock Frisbee - Frisbee Golf":          ItemData("Unlock Sport", ItemType.progression, WSRSport(3, 6)),
    "Unlock Archery":                         ItemData("Unlock Sport", ItemType.progression, WSRSport(4, 7)),
    "Unlock Basketball - 3 Point Contest":    ItemData("Unlock Sport", ItemType.progression, WSRSport(5, 8)),
    "Unlock Basketball - Pickup Game":        ItemData("Unlock Sport", ItemType.progression, WSRSport(5, 9)),
    "Unlock Table Tennis - Return Challenge": ItemData("Unlock Sport", ItemType.progression, WSRSport(6, 10)),
    "Unlock Table Tennis - Match":            ItemData("Unlock Sport", ItemType.progression, WSRSport(6, 11)),
    "Unlock Golf":                            ItemData("Unlock Sport", ItemType.progression, WSRSport(7, 12)),
    "Unlock Bowling - 10 Pin Game":           ItemData("Unlock Sport", ItemType.progression, WSRSport(8, 13)),
    "Unlock Bowling - 100 Pin Game":          ItemData("Unlock Sport", ItemType.progression, WSRSport(8, 14)),
    "Unlock Bowling - Spin Control":          ItemData("Unlock Sport", ItemType.progression, WSRSport(8, 15)),
    "Unlock Power Cruising":                  ItemData("Unlock Sport", ItemType.progression, WSRSport(9, 16)),
    "Unlock Canoeing":                        ItemData("Unlock Sport", ItemType.progression, WSRSport(10, 17)),
    "Unlock Cycling":                         ItemData("Unlock Sport", ItemType.progression, WSRSport(11, 18)),
    "Unlock Air Sports - Skydiving":          ItemData("Unlock Sport", ItemType.progression, WSRSport(12, 19)),
    "Unlock Air Sports - Island Flyover":     ItemData("Unlock Sport", ItemType.progression, WSRSport(12, 20)),

    #Level Unlocks
    "Unlock Swordplay Showdown - Bridge":             ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Lighthouse":         ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Beach":              ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Mountain":           ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Forest":             ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Ruins":              ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Waterfall":          ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Cliffs":             ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Castle":             ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Volcano":            ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Bridge Reverse":     ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Lighthouse Reverse": ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Beach Reverse":      ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Mountain Reverse":   ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Forest Reverse":     ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Ruins Reverse":      ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Waterfall Reverse":  ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Cliffs Reverse":     ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Castle Reverse":     ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Swordplay Showdown - Volcano Reverse":    ItemData("Unlock Level", ItemType.progression, WSRSport(1,3)),
    "Unlock Wakeboarding - Beginner":                 ItemData("Unlock Level", ItemType.progression, WSRSport(2,4)),
    "Unlock Wakeboarding - Intermediate":             ItemData("Unlock Level", ItemType.progression, WSRSport(2,4)),
    "Unlock Wakeboarding - Expert":                   ItemData("Unlock Level", ItemType.progression, WSRSport(2,4)),
    "Unlock Frisbee Golf - Classic A":                ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Classic B":                ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Classic C":                ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Resort A":                 ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Resort B":                 ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Resort C":                 ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Special":                  ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Classic 9":                ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - Resort 9":                 ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Frisbee Golf - 18 Hole":                  ItemData("Unlock Level", ItemType.progression, WSRSport(3,6)),
    "Unlock Archery - Beginner":                      ItemData("Unlock Level", ItemType.progression, WSRSport(4,7)),
    "Unlock Archery - Intermediate":                  ItemData("Unlock Level", ItemType.progression, WSRSport(4,7)),
    "Unlock Archery - Expert":                        ItemData("Unlock Level", ItemType.progression, WSRSport(4,7)),
    "Unlock Archery - Expert":                        ItemData("Unlock Level", ItemType.progression, WSRSport(4,7)),
    "Unlock Golf - Classic A":                        ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Classic B":                        ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Classic C":                        ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Resort A":                         ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Resort B":                         ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Resort C":                         ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Special":                          ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Classic 9":                        ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - Resort 9":                         ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Golf - 18 Hole":                          ItemData("Unlock Level", ItemType.progression, WSRSport(7,12)),
    "Unlock Power Cruising - Beach":                  ItemData("Unlock Level", ItemType.progression, WSRSport(9,16)),
    "Unlock Power Cruising - Lagoon":                 ItemData("Unlock Level", ItemType.progression, WSRSport(9,16)),
    "Unlock Power Cruising - Lighthouse":             ItemData("Unlock Level", ItemType.progression, WSRSport(9,16)),
    "Unlock Power Cruising - Marina":                 ItemData("Unlock Level", ItemType.progression, WSRSport(9,16)),
    "Unlock Power Cruising - Cavern":                 ItemData("Unlock Level", ItemType.progression, WSRSport(9,16)),
    "Unlock Power Cruising - Shoals":                 ItemData("Unlock Level", ItemType.progression, WSRSport(9,16)),
    "Unlock Cycling - Around The Island":             ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - To The Beach":                  ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - Across The Bridge":             ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - Over Talon Rock":               ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - Up The Volcano":                ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - Into Maka Wuhu":                ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - 3-Stage Race A":                ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - 3-Stage Race B":                ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Cycling - 6 Stage":                       ItemData("Unlock Level", ItemType.progression, WSRSport(11,18)),
    "Unlock Island Flyover - Daytime":                ItemData("Unlock Level", ItemType.progression, WSRSport(12,20)),
    "Unlock Island Flyover - Evening":                ItemData("Unlock Level", ItemType.progression, WSRSport(12,20)),
    "Unlock Island Flyover - Night":                  ItemData("Unlock Level", ItemType.progression, WSRSport(12,20)),

    #Sport Timers
    "Wakeboard Timer":           ItemData("Timer", ItemType.progression_skip_balancing, WSRSport(2,4)),
    "Basketball (3PC) Timer":    ItemData("Timer", ItemType.progression_skip_balancing, WSRSport(5,8)),
    "Basketball (Pickup) Timer": ItemData("Timer", ItemType.progression_skip_balancing, WSRSport(5,9)),
    "Power Cruising Timer":      ItemData("Timer", ItemType.progression_skip_balancing, WSRSport(9,16)),
    "Canoeing Timer":            ItemData("Timer", ItemType.progression_skip_balancing, WSRSport(10,17)),
    "Island Flyover Timer":      ItemData("Timer", ItemType.progression_skip_balancing, WSRSport(12,20)),

    #Extra Progression Items
    "Progressive Frisbee (Frisbee Dog)":           ItemData("Progression", ItemType.progression, WSRSport(3,5)),
    "Progressive Frisbee (Frisbee Golf)":          ItemData("Progression", ItemType.progression, WSRSport(3,6)),
    "Progressive Arrow (Archery)":                 ItemData("Progression", ItemType.progression, WSRSport(4,7)),
    "Progressive Fruit (Archery)":                 ItemData("Progression", ItemType.progression, WSRSport(4,7)),
    "Basketball (3-Point Contest) - Golden Balls": ItemData("Progression", ItemType.progression, WSRSport(5,8)),
    "Basketball Pickup Game - Dunk":               ItemData("Progression", ItemType.progression, WSRSport(5,9)),
    "Table Tennis (Return Challenge) - Cans":      ItemData("Progression", ItemType.progression, WSRSport(6,7)),
    "Progressive Club (Golf)":                     ItemData("Progression", ItemType.progression, WSRSport(7,12)),
    "Golf - Turning":                              ItemData("Progression", ItemType.progression, WSRSport(7,12)),
    "Bowling (Standard) - Turning":                ItemData("Progression", ItemType.progression, WSRSport(8,13)),
    "Bowling (Standard) - Moving":                 ItemData("Progression", ItemType.progression, WSRSport(8,13)),
    "Bowling (Standard) - Spin":                   ItemData("Progression", ItemType.progression, WSRSport(8,13)),
    "Bowling (100 Pin) - Turning":                 ItemData("Progression", ItemType.progression, WSRSport(8,14)),
    "Bowling (100 Pin) - Moving":                  ItemData("Progression", ItemType.progression, WSRSport(8,14)),
    "Bowling (100 Pin) - Spin":                    ItemData("Progression", ItemType.progression, WSRSport(8,14)),
    "Bowling (Spin Control) - Turning":            ItemData("Progression", ItemType.progression, WSRSport(8,15)),
    "Bowling (Spin Control) - Moving":             ItemData("Progression", ItemType.progression, WSRSport(8,15)),
    "Bowling (Spin Control) - Spin":               ItemData("Progression", ItemType.progression, WSRSport(8,15)),
    "Power Cruising - Boost":                      ItemData("Progression", ItemType.progression, WSRSport(9,16)),
    "Progressive Ring Timer - Power Cruising":     ItemData("Progression", ItemType.progression, WSRSport(9,16)),
    "Progressive Heart - Cycling":                 ItemData("Progression", ItemType.progression, WSRSport(11,18)),
    "Cycling - Drafting":                          ItemData("Progression", ItemType.progression, WSRSport(11,18)),

    #Useful Items
    "Swordplay Duel - Blocking":           ItemData("Useful", ItemType.useful, WSRSport(1,1)),
    "Swordplay Speed Slice - Pausing":     ItemData("Useful", ItemType.useful, WSRSport(1,2)),
    "Swordplay Showdown - Blocking":       ItemData("Useful", ItemType.useful, WSRSport(1,3)),
    "Progressive Hearts - Swordplay":      ItemData("Useful", ItemType.useful, WSRSport(1,3)),
    "Frisbee Dog - A+2 Balloon Pop":       ItemData("Useful", ItemType.useful, WSRSport(3,6)),
    "Archery - Aiming Circle":             ItemData("Useful", ItemType.useful, WSRSport(4,7)),
    "Basketball Pickup Game - Passing":    ItemData("Useful", ItemType.useful, WSRSport(5,9)),
    "Basketball Pickup Game - 3-Pointers": ItemData("Useful", ItemType.useful, WSRSport(5,9)),
    "Table Tennis - Spin":                 ItemData("Useful", ItemType.useful, WSRSport(6,11)),
    "Table Tennis - Smash Hit":            ItemData("Useful", ItemType.useful, WSRSport(6,11)),
    "Golf - HUD":                          ItemData("Useful", ItemType.useful, WSRSport(7,12)),
    "Golf - Backspin":                     ItemData("Useful", ItemType.useful, WSRSport(7,12)),
    "Golf - Green Low View":               ItemData("Useful", ItemType.useful, WSRSport(7,12)),
    "Golf - Green Slope View":             ItemData("Useful", ItemType.useful, WSRSport(7,12)),

    #Garbage Items
    "100 Skill Points (Swordplay Duel)":                  ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Swordplay Speed Slice)":           ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Swordplay Showdown)":              ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Wakeboarding)":                    ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Frisbee Dog)":                     ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Frisbee Golf)":                    ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Archery)":                         ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Basketball - 3 Point Contest)":    ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Basketball - Pickup Game)":        ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Table Tennis - Return Challenge)": ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Table Tennis - Match)":            ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Golf)":                            ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Bowling - 10-pin Game)":           ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Bowling - 100-pin Game)":          ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Bowling - Spin Control)":          ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Power Cruising)":                  ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Canoeing)":                        ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Cycling)":                         ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "100 Skill Points (Air Sports - Skydiving)":          ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "Extra Max Heart (Swordplay Showdown)":               ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "Extra Max Heart (Cycling)":                          ItemData("Filler", ItemType.filler, WSRSport(0,0)),
    "Random Cosmetic":                                    ItemData("Filler", ItemType.filler, WSRSport(0,0)),
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