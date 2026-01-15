from BaseClasses import Region, Entrance, ItemClassification, Location, LocationProgressType
from .types import CategoryIndex, SportIndex, WSRLocation, WSRItem
from .LocationList import location_table
from typing import TYPE_CHECKING, List, Dict, Optional
from .options import SportsUnlockState

if TYPE_CHECKING:
    from . import WSRWorld


# CategoryIndex: region
category_regions = {
    CategoryIndex.SWORDPLAY: "Swordplay",
    CategoryIndex.WAKEBOARD: "Wakeboarding",
    CategoryIndex.FRISBEE: "Frisbee",
    CategoryIndex.ARCHERY: "Archery",
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
    # -------------------------------------------- HUB ----------------------------------------------- #
    title_screen = create_region(world, "Title Screen")
    menu = create_region_and_connect(world, "Menu", "Title Screen -> Menu", title_screen)

    # ------------------------------------------ Swordplay ------------------------------------------- #
    swordplay_region = create_region_and_connect(world, "Swordplay Region", "Menu -> Swordplay", menu)
    duel = create_region_and_connect(world, "Duel", "Swordplay Menu -> Duel", swordplay_region)
    speed_slice = create_region_and_connect(world, "Speed Slice", "Swordplay Menu -> Speed Slice", swordplay_region)

    #Showdown Regions:
    showdown_region = create_region_and_connect(world, "Showdown Menu", "Swordplay Menu -> Showdown Menu", swordplay_region)
    showdown_normal_region = create_region_and_connect(world, "Showdown Normal Levels", "Showdown Menu -> Normal", showdown_region)
    showdown_reverse_region = create_region_and_connect(world, "Showdown Reverse Levels", "Showdown Menu -> Reverse", showdown_region)

    #Showdown Levels:
    sgl_lev1 = create_region_and_connect(world, "Bridge", "Swordplay Showdown - Level 1", showdown_normal_region)
    sgl_lev2 = create_region_and_connect(world, "Showdown - Lighthouse", "Swordplay Showdown - Level 2", showdown_normal_region)
    sgl_lev3 = create_region_and_connect(world, "Showdown - Beach", "Swordplay Showdown - Level 3", showdown_normal_region)
    sgl_lev4 = create_region_and_connect(world, "Mountain", "Swordplay Showdown - Level 4", showdown_normal_region)
    sgl_lev5 = create_region_and_connect(world, "Forest", "Swordplay Showdown - Level 5", showdown_normal_region)
    sgl_lev6 = create_region_and_connect(world, "Ruins", "Swordplay Showdown - Level 6", showdown_normal_region)
    sgl_lev7 = create_region_and_connect(world, "Waterfall", "Swordplay Showdown - Level 7", showdown_normal_region)
    sgl_lev8 = create_region_and_connect(world, "Cliffs", "Swordplay Showdown - Level 8", showdown_normal_region)
    sgl_lev9 = create_region_and_connect(world, "Castle", "Swordplay Showdown - Level 9", showdown_normal_region)
    sgl_lev10 = create_region_and_connect(world, "Volcano", "Swordplay Showdown - Level 10", showdown_normal_region)
    sgl_lev11 = create_region_and_connect(world, "Bridge Reverse", "Swordplay Showdown - Reverse Level 1", showdown_reverse_region)
    sgl_lev12 = create_region_and_connect(world, "Lighthouse Reverse", "Swordplay Showdown - Reverse Level 2", showdown_reverse_region)
    sgl_lev13 = create_region_and_connect(world, "Beach Reverse", "Swordplay Showdown - Reverse Level 3", showdown_reverse_region)
    sgl_lev14 = create_region_and_connect(world, "Mountain Reverse", "Swordplay Showdown - Reverse Level 4", showdown_reverse_region)
    sgl_lev15 = create_region_and_connect(world, "Forest Reverse", "Swordplay Showdown - Reverse Level 5", showdown_reverse_region)
    sgl_lev16 = create_region_and_connect(world, "Ruins Reverse", "Swordplay Showdown - Reverse Level 6", showdown_reverse_region)
    sgl_lev17 = create_region_and_connect(world, "Waterfall Reverse", "Swordplay Showdown - Reverse Level 7", showdown_reverse_region)
    sgl_lev18 = create_region_and_connect(world, "Cliffs Reverse", "Swordplay Showdown - Reverse Level 8", showdown_reverse_region)
    sgl_lev19 = create_region_and_connect(world, "Castle Reverse", "Swordplay Showdown - Reverse Level 9", showdown_reverse_region)
    sgl_lev20 = create_region_and_connect(world, "Volcano Reverse", "Swordplay Showdown - Reverse Level 10", showdown_reverse_region)

    # ------------------------------------------ Wakeboarding ------------------------------------------- #
    wakeboard_region = create_region_and_connect(world, "Wakeboarding Menu", "Menu -> Wakeboarding Menu", menu)
    wakeboard_beginner = create_region_and_connect(world, "Wakeboarding - Beginner", "Wakeboarding Menu -> Beginner", wakeboard_region)
    wakeboard_intermediate = create_region_and_connect(world, "Wakeboarding - Intermediate", "Wakeboarding Menu -> Intermediate", wakeboard_region)
    wakeboard_expert = create_region_and_connect(world, "Wakeboarding - Expert", "Wakeboarding Menu -> Expert", wakeboard_region)

    # ------------------------------------------ Frisbee ------------------------------------------- #
    frisbee_region = create_region_and_connect(world, "Frisbee Menu", "Menu -> Frisbee Menu", menu)
    fdog = create_region_and_connect(world, "Frisbee Dog", "Frisbee Menu -> Frisbee Dog", frisbee_region)
    fgolf_region = create_region_and_connect(world, "Frisbee Golf Menu", "Frisbee Menu -> Frisbee Golf", frisbee_region)

    #Frisbee Golf Modes:
    fgolf_ca = create_region_and_connect(world, "FG - Classic A", "Frisbee Golf Menu -> Classic A", fgolf_region)
    fgolf_cb = create_region_and_connect(world, "FG - Classic B", "Frisbee Golf Menu -> Classic B", fgolf_region)
    fgolf_cc = create_region_and_connect(world, "FG - Classic C", "Frisbee Golf Menu -> Classic C", fgolf_region)
    fgolf_ra = create_region_and_connect(world, "FG - Resort A", "Frisbee Golf Menu -> Resort A", fgolf_region)
    fgolf_rb = create_region_and_connect(world, "FG - Resort B", "Frisbee Golf Menu -> Resort B", fgolf_region)
    fgolf_rc = create_region_and_connect(world, "FG - Resort C", "Frisbee Golf Menu -> Resort C", fgolf_region)
    fgolf_s  = create_region_and_connect(world, "FG - Special", "Frisbee Golf Menu -> Special", fgolf_region)
    fgolf_c9 = create_region_and_connect(world, "FG - Classic Nine", "Frisbee Golf Menu -> Classic", fgolf_region)
    fgolf_r9 = create_region_and_connect(world, "FG - Resort Nine", "Frisbee Golf Menu -> Resort", fgolf_region)
    fgolf_18 = create_region_and_connect(world, "FG - 18 Hole", "Frisbee Golf Menu -> 18 Hole", fgolf_region)

    # ------------------------------------------ Archery ------------------------------------------- #
    archery = create_region_and_connect(world, "Archery", "Menu -> Archery", menu)

    # ----------------------------------------- Basketball ----------------------------------------- #
    basketball_region = create_region_and_connect(world, "Basketball Menu", "Menu -> Basketball Menu", menu)
    bsk_3pt = create_region_and_connect(world, "Basketball - 3 Point Contest", "Basketball Menu -> 3pt", basketball_region)
    bsk_vs  = create_region_and_connect(world, "Basketball - Pickup Game", "Basketball Menu -> VS", basketball_region)

    # ---------------------------------------- Table Tennis ----------------------------------------- #
    table_tennis_region = create_region_and_connect(world, "Table Tennis Menu", "Menu -> Table Tennis Menu", menu)
    png_ret = create_region_and_connect(world, "Table Tennis - Return Challenge", "Table Tennis Menu -> Return Challenge", table_tennis_region)
    png_vs  = create_region_and_connect(world, "Table Tennis - Match", "Table Tennis Menu -> Match", table_tennis_region) 

    # -------------------------------------------- Golf --------------------------------------------- #
    golf_region = create_region_and_connect(world, "Golf Menu", "Menu -> Golf Menu", menu)

    #Golf Modes:
    golf_ca = create_region_and_connect(world, "Golf - Classic A", "Golf Menu -> Classic A", golf_region)
    golf_cb = create_region_and_connect(world, "Golf - Classic B", "Golf Menu -> Classic B", golf_region)
    golf_cc = create_region_and_connect(world, "Golf - Classic C", "Golf Menu -> Classic C", golf_region)
    golf_ra = create_region_and_connect(world, "Golf - Resort A", "Golf Menu -> Resort A", golf_region)
    golf_rb = create_region_and_connect(world, "Golf - Resort B", "Golf Menu -> Resort B", golf_region)
    golf_rc = create_region_and_connect(world, "Golf - Resort C", "Golf Menu -> Resort C", golf_region)
    golf_s  = create_region_and_connect(world, "Golf - Special", "Golf Menu -> Special", golf_region)
    golf_c9 = create_region_and_connect(world, "Golf - Classic Nine", "Golf Menu -> Classic", golf_region)
    golf_r9 = create_region_and_connect(world, "Golf - Resort Nine", "Golf Menu -> Resort", golf_region)
    golf_18 = create_region_and_connect(world, "Golf - 18 Hole", "Golf Menu -> 18 Hole", golf_region)

    # ------------------------------------------- Bowling --------------------------------------------- #
    bowling_menu = create_region_and_connect(world, "Bowling Menu", "Menu -> Bowling Menu", menu)
    bwl_std = create_region_and_connect(world, "Bowling - Standard Game", "Bowling Menu -> Standard", bowling_menu)
    bwl_100 = create_region_and_connect(world, "Bowling - 100 Pin Game", "Bowling Menu -> 100", bowling_menu)
    bwl_wal = create_region_and_connect(world, "Bowling - Spin Control", "Bowling Menu -> Spin Control", bowling_menu)

    # ---------------------------------------- Power Cruising ------------------------------------------ #
    jsk_menu = create_region_and_connect(world, "Power Cruising Menu", "Menu -> Power Cruising Menu", menu)
    jsk_lev1 = create_region_and_connect(world, "Power Cruising - Beach", "Power Cruising Level 1", jsk_menu)
    jsk_lev2 = create_region_and_connect(world, "Lagoon", "Power Cruising Level 2", jsk_menu)
    jsk_lev3 = create_region_and_connect(world, "Power Cruising - Lighthouse", "Power Cruising Level 3", jsk_menu)
    jsk_lev4 = create_region_and_connect(world, "Marina", "Power Cruising Level 4", jsk_menu)
    jsk_lev5 = create_region_and_connect(world, "Cavern", "Power Cruising Level 5", jsk_menu)
    jsk_lev6 = create_region_and_connect(world, "Shoals", "Power Cruising Level 6", jsk_menu)

    # ------------------------------------------- Canoeing --------------------------------------------- #
    can_menu = create_region_and_connect(world, "Canoeing Menu", "Menu -> Canoeing Menu", menu)
    can_beg = create_region_and_connect(world, "Canoeing - Beginner", "Canoeing Menu -> Beginner", can_menu)
    can_int = create_region_and_connect(world, "Canoeing - Intermediate", "Canoeing Menu -> Intermediate", can_menu)
    can_exp = create_region_and_connect(world, "Canoeing - Expert", "Canoeing Menu -> Expert", can_menu)

    # ------------------------------------------- Cycling ---------------------------------------------- #
    bic_menu = create_region_and_connect(world, "Cycling Menu", "Menu -> Cycling Menu", menu)
    bic_lev1 = create_region_and_connect(world, "Around The Island", "Cycling Menu -> 1", bic_menu)
    bic_lev2 = create_region_and_connect(world, "To The Beach", "Cycling Menu -> 2", bic_menu)
    bic_lev3 = create_region_and_connect(world, "Across The Bridge", "Cycling Menu -> 3", bic_menu)
    bic_lev4 = create_region_and_connect(world, "Over Talon Rock", "Cycling Menu -> 4", bic_menu)
    bic_lev5 = create_region_and_connect(world, "Up The Volcano", "Cycling Menu -> 5", bic_menu)
    bic_lev6 = create_region_and_connect(world, "Into Maka Wuhu", "Cycling Menu -> 6", bic_menu)
    bic_3sa = create_region_and_connect(world, "Cycling - 3 Stage A", "Cycling Menu -> 3race A", bic_menu)
    bic_3sb = create_region_and_connect(world, "Cycling - 3 Stage B", "Cycling Menu -> 3race B", bic_menu)
    bic_6s = create_region_and_connect(world, "Cycling - 6 Stage", "Cycling Menu -> 6 Stage", bic_menu)

    # ------------------------------------------- Air Sports -------------------------------------------- #
    air_sports_menu = create_region_and_connect(world, "Air Sports Menu", "Menu -> Air Sports Menu", menu)
    skydiving = create_region_and_connect(world, "Skydiving", "Air Sports Menu -> Skydiving", air_sports_menu)
    island_flyover = create_region_and_connect(world, "Island Flyover", "Air Sports Menu -> Island Flyover", air_sports_menu)


def create_region(world: "WSRWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    print(f"Name in create_region: {name}")

    for(key, data) in location_table.items():
        if data.region == name:
            location = WSRLocation(world.player, key, data.id, reg)
            reg.locations.append(location)

    world.multiworld.regions.append(reg)

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

# Takes an entrance, removes its old connections, and reconnects it between the two regions specified.
def reconnect_regions(entrance: Entrance, start_region: Region, exit_region: Region):
    if entrance in entrance.connected_region.entrances:
        entrance.connected_region.entrances.remove(entrance)

    if entrance in entrance.parent_region.exits:
        entrance.parent_region.exits.remove(entrance)

    if entrance in start_region.exits:
        start_region.exits.remove(entrance)

    if entrance in exit_region.entrances:
        exit_region.entrances.remove(entrance)

    entrance.parent_region = start_region
    start_region.exits.append(entrance)
    entrance.connect(exit_region)