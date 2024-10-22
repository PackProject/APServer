from BaseClasses import Region, Entrance, ItemClassification, Location, LocationProgressType
from .types import CategoryIndex, SportIndex, WSRLocation, WSRItem
from .locations import location_table, HARD_STAMPS_LOCATIONS, LONG_STAMPS_LOCATIONS
from typing import TYPE_CHECKING, List, Dict, Optional
from .options import SportsUnlockState

if TYPE_CHECKING:
    from . import WSRWorld


# CategoryIndex: region
category_regions = {
    CategoryIndex.SWORDPLAY: "Swordplay",
    CategoryIndex.WAKEBOARD: "Wakeboarding",
    CategoryIndex.FRISBEE: "Frisbee",
    CategoryIndex.ARCHERY: "Archry",
    CategoryIndex.BASKETBALL: "Basketball",
    CategoryIndex.TABLE: "Table Tennis",
    CategoryIndex.GOLF: "Golf",
    CategoryIndex.BOWLING: "Bowling",
    CategoryIndex.CRUISING: "Power Cruising",
    CategoryIndex.CANOE: "Canoeing",
    CategoryIndex.CYCLING: "Cycling",
    CategoryIndex.AIR: "Air Sports",
}

# sports: region
sports_regions = {
    SportIndex.DUEL: "Duel",
    SportIndex.SPEED: "Speed Slice",
    SportIndex.SHOWDOWN: "Showdown",
    SportIndex.WAKEBOARD: "Wakeboarding",
    SportIndex.DOG: "Frisbee Dog",
    SportIndex.FGOLF: "Frisbee Golf",
    SportIndex.ARCHERY: "Archery",
    SportIndex.THREE: "3 Point Contest",
    SportIndex.PICKUP: "Pickup Game",
    SportIndex.RETURN: "Return Challenge",
    SportIndex.MATCH: "Match",
    SportIndex.GOLF: "Golf",
    SportIndex.TEN: "10 Pin",
    SportIndex.HUNDRED: "100 Pin",
    SportIndex.SPIN: "Spin Control",
    SportIndex.CRUISING: "Power Cruising",
    SportIndex.CANOE: "Canoeing",
    SportIndex.CYCLING: "Cycling",
    SportIndex.SKYDIVING: "Skydiving",
    SportIndex.FLYOVER: "Island Flyover",
}

def create_regions(world: "WSRWorld"):
    # ------------------------ HUB --------------------------- #
    title_screen = create_region(world, "Title Screen")
    menu = create_region_and_connect(world, "Menu", "Title Screen -> Menu", title_screen)

def create_region(world: "WSRWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    for(key, data) in location_table.items():
        if data.region == name:
            location = WSRLocation(world.player, key, data.id, reg)
            reg.locations.append(location)

    return reg

def create_region_and_connect(world: "WSRWorld", name: str, \
                              entrancename: str, connected_region: Region, \
                                is_exit: bool = True) -> Region:
    
    reg: Region = create_region(world, name)
    entrance_region: Region
    exit_region: Region

    if is_exit:
        entrance_region = connected_region
        exit_region = reg
    else:
        entrance_region = reg
        exit_region = connected_region

    entrance_region.connect(exit_region, entrancename)
    return reg