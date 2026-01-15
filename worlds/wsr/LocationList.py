from collections import OrderedDict
from typing import NamedTuple, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from . import WSRWorld

#
#   Type Definitions:
#
#   Stamp - Stamp collected from completing some task in a sport
#   Hard Stamp - Stamp that is deemed too hard for casuals to reliably get. These can be removed in logic in settings
#   Long Stamp - Stamp that is deemed too much of a grind to get. These can be removed in logic in settings
#
#   Pro Status - Getting pro status in a sport
#   Champion - Beating the champion in a sport
#   Difficulty - Unlocking the next difficulty in a sport
#   Level - Unlocking the next level in a sport.
# 
#   iPoint - I-Point in Island Flyover (only half ever required)
#   Balloon - White Balloon in Island Flyover (only half ever required)
#
#   Custom - Custom locations added for the randomizer. Example could be getting your first win in Speed Slice
#

class LocData(NamedTuple):
    region: str = None
    location_type: str = None
    category: int = 0
    sport: int = 0
    id: int = 0

def get_total_locations(world: "WSRWorld") -> int:
    total = 0

    for name in location_table.keys():
        if is_location_valid(world, name):
            total += 1

    return total

def is_location_valid(world: "WSRWorld", location: str) -> bool:
    # this currently does absolutely nothing
    if world.options.sports_unlock_state == 0: #change to sports unlock list
        pass

    return True

def get_locations_names() -> Dict[str, int]:
    names = {name: data.id for name, data in location_table.items()}
    return names


#       Location:                                             Type                 Category ID    Sport ID                Location ID        
location_table = OrderedDict([
    #Swordplay Duel
    ("Swordplay Duel - First Win",                            LocData("Duel", 'Custom',            1,             1,                      0x0200)),
    ("Swordplay Duel (Stamp) - Cliff-hanger",                 LocData("Duel", 'Stamp',             1,             1,                      0x0005)),
    ("Swordplay Duel (Stamp) - Straight to the Point",        LocData("Duel", 'Stamp',             1,             1,                      0x0006)),
    ("Swordplay Duel (Stamp) - Met Your Match",               LocData("Duel", 'Stamp',             1,             1,                      0x0007)),
    ("Swordplay Duel (Stamp) - One-Hit Wonder",               LocData("Duel", 'Stamp',             1,             1,                      0x0008)),
    ("Swordplay Duel (Stamp) - Last Mii Standing",            LocData("Duel", 'Impossible Stamp',  1,             1,                      0x0009)),
    ("Swordplay Duel - Pro Status",                           LocData("Duel", 'Pro Status',        1,             1,                      0x0201)),
    ("Swordplay Duel - Beat The Champion (Matt)",             LocData("Duel", 'Champion',          1,             1,                      0x0202)), 
    #Swordplay Speed Slice
    ("Swordplay Speed Slice - First Win",                     LocData("Speed Slice", 'Custom',            1,             2,                      0x0300)),
    ("Swordplay Speed Slice (Stamp) - Slice and Dice",        LocData("Speed Slice", 'Stamp',             1,             2,                      0x000A)),
    ("Swordplay Speed Slice (Stamp) - Slicing Machine",       LocData("Speed Slice", 'Stamp',             1,             2,                      0x000B)),
    ("Swordplay Speed Slice (Stamp) - Psychic Slice",         LocData("Speed Slice", 'Stamp',             1,             2,                      0x000C)),
    ("Swordplay Speed Slice (Stamp) - Double Time",           LocData("Speed Slice", 'Stamp',             1,             2,                      0x000D)),
    ("Swordplay Speed Slice (Stamp) - A Cut Above",           LocData("Speed Slice", 'Impossible Stamp',  1,             2,                      0x000E)),
    ("Swordplay Speed Slice - Pro Status",                    LocData("Speed Slice", 'Pro Status',        1,             2,                      0x0301)),
    ("Swordplay Speed Slice - Beat The Champion (Matt)",      LocData("Speed Slice", 'Champion',          1,             2,                      0x0302)),
    #Swordplay Showdown
    ("Swordplay Showdown - Complete Stage 1",                 LocData("Bridge", 'Custom',            1,             3,                      0x0101)),
    ("Swordplay Showdown - Complete Stage 2",                 LocData("Showdown - Lighthouse", 'Custom',            1,             3,                      0x0102)),
    ("Swordplay Showdown - Complete Stage 3",                 LocData("Showdown - Beach", 'Custom',            1,             3,                      0x0103)),
    ("Swordplay Showdown - Complete Stage 4",                 LocData("Mountain", 'Custom',            1,             3,                      0x0104)),
    ("Swordplay Showdown - Complete Stage 5",                 LocData("Forest", 'Custom',            1,             3,                      0x0105)),
    ("Swordplay Showdown - Complete Stage 6",                 LocData("Ruins", 'Custom',            1,             3,                      0x0106)),
    ("Swordplay Showdown - Complete Stage 7",                 LocData("Waterfall", 'Custom',            1,             3,                      0x0107)),
    ("Swordplay Showdown - Complete Stage 8",                 LocData("Cliffs", 'Custom',            1,             3,                      0x0108)),
    ("Swordplay Showdown - Complete Stage 9",                 LocData("Castle", 'Custom',            1,             3,                      0x0109)),
    ("Swordplay Showdown - Complete Stage 10",                LocData("Volcano", 'Custom',            1,             3,                      0x010A)),
    ("Swordplay Showdown - Complete Stage 11",                LocData("Bridge Reverse", 'Custom',            1,             3,                      0x010B)),
    ("Swordplay Showdown - Complete Stage 12",                LocData("Lighthouse Reverse", 'Custom',            1,             3,                      0x010C)),
    ("Swordplay Showdown - Complete Stage 13",                LocData("Beach Reverse", 'Custom',            1,             3,                      0x010D)),
    ("Swordplay Showdown - Complete Stage 14",                LocData("Mountain Reverse", 'Custom',            1,             3,                      0x010E)),
    ("Swordplay Showdown - Complete Stage 15",                LocData("Forest Reverse", 'Custom',            1,             3,                      0x010F)),
    ("Swordplay Showdown - Complete Stage 16",                LocData("Ruins Reverse", 'Custom',            1,             3,                      0x0110)),
    ("Swordplay Showdown - Complete Stage 17",                LocData("Waterfall Reverse", 'Custom',            1,             3,                      0x0111)),
    ("Swordplay Showdown - Complete Stage 18",                LocData("Cliffs Reverse", 'Custom',            1,             3,                      0x0112)),
    ("Swordplay Showdown - Complete Stage 19",                LocData("Castle Reverse", 'Custom',            1,             3,                      0x0113)),
    ("Swordplay Showdown - Complete Stage 20",                LocData("Volcano Reverse", 'Custom',            1,             3,                      0x0114)),
    ("Swordplay Showdown (Stamp) - Not a Scratch",            LocData("Showdown Menu", 'Stamp',             1,             3,                      0x0000)),
    ("Swordplay Showdown (Stamp) - Sword Fighter",            LocData("Volcano", 'Long Stamp',        1,             3,                      0x0001)),
    ("Swordplay Showdown (Stamp) - Perfect 10",               LocData("Volcano", 'Hard Stamp',        1,             3,                      0x0002)),
    ("Swordplay Showdown (Stamp) - Swordmaster",              LocData("Volcano Reverse", 'Long Stamp',        1,             3,                      0x0003)),
    ("Swordplay Showdown (Stamp) - Untouchable",              LocData("Volcano Reverse", 'Impossible Stamp',  1,             3,                      0x0004)),
    ("Swordplay Showdown - Pro Status",                       LocData("Showdown Menu", 'Pro Status',        1,             3,                      0x0100)),
    #Wakeboarding
    ("Wakeboarding (Stamp) - Huge Air",                       LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x0050)),
    ("Wakeboarding (Stamp) - Bag of Tricks",                  LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x0051)),
    ("Wakeboarding (Stamp) - Smooth Landing",                 LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x0052)),
    ("Wakeboarding (Stamp) - Master Carver",                  LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x0053)),
    ("Wakeboarding (Stamp) - The Long Way Home",              LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x0054)),
    ("Wakeboarding - Pro Status",                             LocData("Wakeboarding Menu", 'Pro Status',        2,             4,                      0x1000)),
    #Frisbee Dog
    ("Frisbee Dog (Stamp) - Good Dog",                        LocData("Frisbee Dog", 'Stamp',             3,             5,                      0x001E)),
    ("Frisbee Dog (Stamp) - Balloon Animal",                  LocData("Frisbee Dog", 'Stamp',             3,             5,                      0x001F)),
    ("Frisbee Dog (Stamp) - A for Effort",                    LocData("Frisbee Dog", 'Hard Stamp',        3,             5,                      0x0020)),
    ("Frisbee Dog (Stamp) - Perfect Target",                  LocData("Frisbee Dog", 'Hard Stamp',        3,             5,                      0x0021)),
    ("Frisbee Dog (Stamp) - Golden Arm",                      LocData("Frisbee Dog", 'Hard Stamp',        3,             5,                      0x0022)),
    ("Frisbee Dog - Pro Status",                              LocData("Frisbee Dog", 'Pro Status',        3,             5,                      0x0700)),
    #Frisbee Golf
    ("Frisbee Golf - Complete Hole 1",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1501)),
    ("Frisbee Golf - Complete Hole 2",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1502)),
    ("Frisbee Golf - Complete Hole 3",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1503)),
    ("Frisbee Golf - Complete Hole 4",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1504)),
    ("Frisbee Golf - Complete Hole 5",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1505)),
    ("Frisbee Golf - Complete Hole 6",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1506)),
    ("Frisbee Golf - Complete Hole 7",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1507)),
    ("Frisbee Golf - Complete Hole 8",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1508)),
    ("Frisbee Golf - Complete Hole 9",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1509)),
    ("Frisbee Golf - Complete Hole 10",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x150A)),
    ("Frisbee Golf - Complete Hole 11",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x150B)),
    ("Frisbee Golf - Complete Hole 12",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x150C)),
    ("Frisbee Golf - Complete Hole 13",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x150D)),
    ("Frisbee Golf - Complete Hole 14",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x150E)),
    ("Frisbee Golf - Complete Hole 15",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x150F)),
    ("Frisbee Golf - Complete Hole 16",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1510)),
    ("Frisbee Golf - Complete Hole 17",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1511)),
    ("Frisbee Golf - Complete Hole 18",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1512)),
    ("Frisbee Golf - Complete Hole 19",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1513)),
    ("Frisbee Golf - Complete Hole 20",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1514)),
    ("Frisbee Golf - Complete Hole 21",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1515)),            
    ("Frisbee Golf - Get a par",                              LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1516)),
    ("Frisbee Golf - Get a birdie",                           LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1517)),
    ("Frisbee Golf - Get an eagle",                           LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x1518)),
    ("Frisbee Golf (Stamp) - Under Par",                      LocData("Frisbee Golf Menu", 'Stamp',             3,             6,                      0x0064)),
    ("Frisbee Golf (Stamp) - Lucky Skip",                     LocData("Frisbee Golf Menu", 'Stamp',             3,             6,                      0x0065)),
    ("Frisbee Golf (Stamp) - On a Roll",                      LocData("Frisbee Golf Menu", 'Hard Stamp',        3,             6,                      0x0066)),
    ("Frisbee Golf (Stamp) - Hole in One",                    LocData("Frisbee Golf Menu", 'Stamp',             3,             6,                      0x0067)),
    ("Frisbee Golf (Stamp) - Straight and Narrow",            LocData("Frisbee Golf Menu", 'Impossible Stamp',  3,             6,                      0x0068)),
    ("Frisbee Golf - Pro Status",                             LocData("Frisbee Golf Menu", 'Pro Status',        3,             6,                      0x1500)), 
    #Archery
    ("Archery (Stamp) - Bull Stampede",                       LocData("Archery", 'Stamp',             4,             7,                      0x0019)),
    ("Archery (Stamp) - Sure Shot",                           LocData("Archery", 'Stamp',             4,             7,                      0x001A)),
    ("Archery (Stamp) - Century Shot",                        LocData("Archery", 'Long Stamp',        4,             7,                      0x001B)),
    ("Archery (Stamp) - A Secret to Everybody",               LocData("Archery", 'Hard Stamp',        4,             7,                      0x001C)),
    ("Archery (Stamp) - Sharpshooter",                        LocData("Archery", 'Impossible Stamp',  4,             7,                      0x001D)),
    ("Archery - Pro Status",                                  LocData("Archery", 'Pro Status',        4,             7,                      0x0600)),
    #Basketball 3-Point Contest
    ("3-Point Contest (Stamp) - Hot Streak",                  LocData("Basketball - 3 Point Contest", 'Stamp',             5,             8,                      0x0023)),
    ("3-Point Contest (Stamp) - Bonus Plumber",               LocData("Basketball - 3 Point Contest", 'Stamp',             5,             8,                      0x0024)),
    ("3-Point Contest (Stamp) - Quick Draw",                  LocData("Basketball - 3 Point Contest", 'Hard Stamp',        5,             8,                      0x0025)),
    ("3-Point Contest (Stamp) - Hot Hand",                    LocData("Basketball - 3 Point Contest", 'Impossible Stamp',  5,             8,                      0x0026)),
    ("3-Point Contest (Stamp) - Pure Shooter",                LocData("Basketball - 3 Point Contest", 'Impossible Stamp',  5,             8,                      0x0027)),
    ("3-Point Contest - Pro Status",                          LocData("Basketball - 3 Point Contest", 'Pro Status',        5,             8,                      0x0800)),
    #Basketball Pickup Game
    ("Pickup Game (Stamp) - Triple Dip",                      LocData("Basketball - Pickup Game", 'Stamp',             5,             9,                      0x0028)),
    ("Pickup Game (Stamp) - Rim Rattler",                     LocData("Basketball - Pickup Game", 'Stamp',             5,             9,                      0x0029)),
    ("Pickup Game (Stamp) - Lights Out",                      LocData("Basketball - Pickup Game", 'Hard Stamp',        5,             9,                      0x002A)),
    ("Pickup Game (Stamp) - Buzzer Beater",                   LocData("Basketball - Pickup Game", 'Hard Stamp',        5,             9,                      0x002B)),
    ("Pickup Game (Stamp) - Hoop Hero",                       LocData("Basketball - Pickup Game", 'Impossible Stamp',  5,             9,                      0x002C)),
    ("Pickup Game - Pro Status",                              LocData("Basketball - Pickup Game", 'Pro Status',        5,             9,                      0x0900)),
    ("Pickup Game (Stamp) - Beat The Champion (Tommy)",       LocData("Basketball - Pickup Game", 'Champion',          5,             9,                      0x0901)),
    #Table Tennis
    ("Table Tennis Match (Stamp) - In Your Face",             LocData("Table Tennis - Match", 'Stamp',             6,             10,                     0x004B)),
    ("Table Tennis Match (Stamp) - Back from the Brink",      LocData("Table Tennis - Match", 'Hard Stamp',        6,             10,                     0x004C)),
    ("Table Tennis Match (Stamp) - Epic Rally",               LocData("Table Tennis - Match", 'Hard Stamp',        6,             10,                     0x004D)),
    ("Table Tennis Match (Stamp) - Perfectly Matched",        LocData("Table Tennis - Match", 'Hard Stamp',        6,             10,                     0x004E)),
    ("Table Tennis Match (Stamp) - Table Titan",              LocData("Table Tennis - Match", 'Impossible Stamp',  6,             10,                     0x004F)),
    ("Table Tennis Match - Pro Status",                       LocData("Table Tennis - Match", 'Pro Status',        6,             10,                     0x0F00)),
    ("Table Tennis Match - Beat The Champion (Lucia)",        LocData("Table Tennis - Match", 'Champion',          6,             10,                     0x0F01)),
    #Table Tennis Return Challenge
    ("Return Challenge (Stamp) - 50-pointer",                 LocData("Table Tennis - Return Challenge", 'Stamp',             6,             11,                     0x0046)),
    ("Return Challenge (Stamp) - 100-pointer",                LocData("Table Tennis - Return Challenge", 'Hard Stamp',        6,             11,                     0x0047)),
    ("Return Challenge (Stamp) - 200-pointer",                LocData("Table Tennis - Return Challenge", 'Impossible Stamp',  6,             11,                     0x0048)),
    ("Return Challenge (Stamp) - Recycler",                   LocData("Table Tennis - Return Challenge", 'Impossible Stamp',  6,             11,                     0x0049)),
    ("Return Challenge (Stamp) - Save Face",                  LocData("Table Tennis - Return Challenge", 'Impossible Stamp',  6,             11,                     0x004A)),
    ("Return Challenge - Pro Status",                         LocData("Table Tennis - Return Challenge", 'Pro Status',        6,             11,                     0x0E00)),
    #Golf
    ("Golf - Complete Hole 1",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1400)),
    ("Golf - Complete Hole 2",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1401)),
    ("Golf - Complete Hole 3",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1402)),
    ("Golf - Complete Hole 4",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1403)),
    ("Golf - Complete Hole 5",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1404)),
    ("Golf - Complete Hole 6",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1405)),
    ("Golf - Complete Hole 7",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1406)),
    ("Golf - Complete Hole 8",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1407)),
    ("Golf - Complete Hole 9",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x1408)),
    ("Golf - Complete Hole 10",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x1409)),
    ("Golf - Complete Hole 11",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x140A)),
    ("Golf - Complete Hole 12",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x140B)),
    ("Golf - Complete Hole 13",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x140C)),
    ("Golf - Complete Hole 14",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x140D)),
    ("Golf - Complete Hole 15",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x140E)),
    ("Golf - Complete Hole 16",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x140F)),
    ("Golf - Complete Hole 17",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x1410)),
    ("Golf - Complete Hole 18",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x1411)),
    ("Golf - Complete Hole 19",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x1412)),
    ("Golf - Complete Hole 20",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x1413)),
    ("Golf - Complete Hole 21",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x1414)),
    ("Golf - Par",                                            LocData("Golf Menu", 'Custom',            7,             12,                     0x1415)),
    ("Golf - Birdie",                                         LocData("Golf Menu", 'Custom',            7,             12,                     0x1416)),
    ("Golf - Eagle",                                          LocData("Golf Menu", 'Custom',            7,             12,                     0x1417)),
    ("Golf (Stamp) - Under Par",                              LocData("Golf Menu", 'Stamp',             7,             12,                     0x005F)),
    ("Golf (Stamp) - Chip In",                                LocData("Golf Menu", 'Stamp',             7,             12,                     0x0060)),
    ("Golf (Stamp) - King of Clubs",                          LocData("Golf Menu", 'Hard Stamp',        7,             12,                     0x0061)),
    ("Golf (Stamp) - Ace of Clubs",                           LocData("Golf Menu", 'Impossible Stamp',  7,             12,                     0x0062)),
    ("Golf (Stamp) - Hole in One",                            LocData("Golf Menu", 'Impossible Stamp',  7,             12,                     0x0063)),
    ("Golf - Pro Status",                                     LocData("Golf Menu", 'Pro Status',        7,             12,                     0x1418)),         
    #Bowling 10 Pin
    ("Bowling 10 Pin - First Strike",                         LocData("Bowling - Standard Game", 'Custom',            8,             13,                     0x0A00)),
    ("Bowling Standard (Stamp) - Gobble Gobble",              LocData("Bowling - Standard Game", 'Stamp',             8,             13,                     0x002D)),
    ("Bowling Standard (Stamp) - Split Spare",                LocData("Bowling - Standard Game", 'Stamp',             8,             13,                     0x002E)),
    ("Bowling Standard (Stamp) - High Roller",                LocData("Bowling - Standard Game", 'Hard Stamp',        8,             13,                     0x002F)),
    ("Bowling Standard (Stamp) - Pin Dropper",                LocData("Bowling - Standard Game", 'Hard Stamp',        8,             13,                     0x0030)),
    ("Bowling Standard (Stamp) - Perfect Game",               LocData("Bowling - Standard Game", 'Impossible Stamp',  8,             13,                     0x0031)),
    ("Bowling Standard - Pro Status",                         LocData("Bowling - Standard Game", 'Pro Status',        8,             13,                     0x0A01)),      
    #Bowling 100 Pin
    ("Bowling 100-Pin - First Strike",                        LocData("Bowling - 100 Pin Game", 'Custom',            8,             14,                     0x0B01)),
    ("Bowling 100-Pin (Stamp) - Super Strike",                LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x0032)),
    ("Bowling 100-Pin (Stamp) - Split Spare",                 LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x0033)),
    ("Bowling 100-Pin (Stamp) - Off the Wall",                LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x0034)),
    ("Bowling 100-Pin (Stamp) - Secret Strike",               LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x0035)),
    ("Bowling 100-Pin (Stamp) - Pin Dropper",                 LocData("Bowling - 100 Pin Game", 'Hard Stamp',        8,             14,                     0x0036)),
    ("Bowling 100-Pin - Pro Status",                          LocData("Bowling - 100 Pin Game", 'Pro Status',        8,             14,                     0x0B00)),
    #Bowling Spin Control
    ("Spin Control - First Strike",                           LocData("Bowling - Spin Control", 'Custom',            8,             15,                     0x0C01)),
    ("Spin Control (Stamp) - One for All",                    LocData("Bowling - Spin Control", 'Stamp',             8,             15,                     0x0037)),
    ("Spin Control (Stamp) - Split Spare",                    LocData("Bowling - Spin Control", 'Stamp',             8,             15,                     0x0038)),
    ("Spin Control (Stamp) - Head First",                     LocData("Bowling - Spin Control", 'Stamp',             8,             15,                     0x0039)),
    ("Spin Control (Stamp) - English Major",                  LocData("Bowling - Spin Control", 'Hard Stamp',        8,             15,                     0x003A)),
    ("Spin Control (Stamp) - Pin Dropper",                    LocData("Bowling - Spin Control", 'Hard Stamp',        8,             15,                     0x003B)),
    ("Spin Control - Pro Status",                             LocData("Bowling - Spin Control", 'Pro Status',        8,             15,                     0x0C00)),     
    #Power Cruising
    ("Power Cruising (Stamp) - Ringmaster",                   LocData("Power Cruising Menu", 'Stamp',             9,             16,                     0x000F)),
    ("Power Cruising (Stamp) - 5,000-Pointer",                LocData("Power Cruising Menu", 'Long Stamp',        9,             16,                     0x0010)),
    ("Power Cruising (Stamp) - Power Cruiser",                LocData("Power Cruising Menu", 'Hard Stamp',        9,             16,                     0x0011)),
    ("Power Cruising (Stamp) - Power Jumper",                 LocData("Power Cruising Menu", 'Stamp',             9,             16,                     0x0012)),
    ("Power Cruising (Stamp) - Leisure Cruiser",              LocData("Power Cruising Menu", 'Long Stamp',        9,             16,                     0x0013)),
    ("Power Cruising - Pro Status",                           LocData("Power Cruising Menu", 'Pro Status',        9,             16,                     0x0400)),
    ("Power Cruising - 1,500 Total Points",                   LocData("Power Cruising Menu", 'Custom',            9,             16,                     0x0401)),
    #Canoeing
    ("Canoeing (Stamp) - Beginner License",                   LocData("Canoeing Menu", 'Stamp',            10,             17,                     0x0041)),
    ("Canoeing (Stamp) - Intermediate License",               LocData("Canoeing Menu", 'Hard Stamp',       10,             17,                     0x0042)),
    ("Canoeing (Stamp) - Expert License",                     LocData("Canoeing Menu", 'Impossible Stamp', 10,             17,                     0x0043)),
    ("Canoeing (Stamp) - Ducks in a Row",                     LocData("Canoeing Menu", 'Stamp',            10,             17,                     0x0044)),
    ("Canoeing (Stamp) - Cut the Red Tape",                   LocData("Canoeing Menu", 'Impossible Stamp', 10,             17,                     0x0045)),
    ("Canoeing - Pro Status",                                 LocData("Canoeing Menu", 'Pro Status',       10,             17,                     0x0D01)),
    #Cycling
    ("Cycling - Complete Stage 1",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x1701)),
    ("Cycling - Complete Stage 2",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x1702)),
    ("Cycling - Complete Stage 3",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x1703)),
    ("Cycling - Complete Stage 4",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x1704)),
    ("Cycling - Complete Stage 5",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x1705)),
    ("Cycling - Complete Stage 6",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x1706)),
    ("Cycling (Stamp) - Last Gasp",                           LocData("Cycling Menu", 'Stamp',            11,             18,                     0x006E)),
    ("Cycling (Stamp) - First of Many",                       LocData("Cycling Menu", 'Stamp',            11,             18,                     0x006F)),
    ("Cycling (Stamp) - 1-Stage Master",                      LocData("Cycling Menu", 'Long Stamp',       11,             18,                     0x0070)),
    ("Cycling (Stamp) - 3-Stage Master",                      LocData("Cycling Menu", 'Long Stamp',       11,             18,                     0x0071)),
    ("Cycling (Stamp) - 6-Stage Master",                      LocData("Cycling Menu", 'Long Stamp',       11,             18,                     0x0072)),
    ("Cycling - Pro Status",                                  LocData("Cycling Menu", 'Pro Status',       11,             18,                     0x1700)),
    #Skydiving
    ("Skydiving (Stamp) - High Five",                         LocData("Skydiving", 'Stamp',            12,             19,                     0x0073)),
    ("Skydiving (Stamp) - For the Birds",                     LocData("Skydiving", 'Hard Stamp',       12,             19,                     0x0074)),
    ("Skydiving (Stamp) - Friends in High Places",            LocData("Skydiving", 'Stamp',            12,             19,                     0x0075)),
    ("Skydiving (Stamp) - Camera Shy",                        LocData("Skydiving", 'Stamp',            12,             19,                     0x0076)),
    ("Skydiving (Stamp) - 200-point Dive",                    LocData("Skydiving", 'Hard Stamp',       12,             19,                     0x0077)),
    ("Skydiving - Pro Status",                                LocData("Skydiving", 'Pro Status',       12,             19,                     0x1800)),
    #Island Flyover
    ("Island Flyover - Progressive I-Point Group (1)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B00)),
    ("Island Flyover - Progressive I-Point Group (2)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B01)),
    ("Island Flyover - Progressive I-Point Group (3)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B02)),
    ("Island Flyover - Progressive I-Point Group (4)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B03)),
    ("Island Flyover - Progressive I-Point Group (5)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B04)),
    ("Island Flyover - Progressive I-Point Group (6)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B05)),
    ("Island Flyover - Progressive I-Point Group (7)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B06)),
    ("Island Flyover - Progressive I-Point Group (8)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B07)),
    ("Island Flyover - Progressive I-Point Group (9)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x1B08)),
    ("Island Flyover - Progressive I-Point Group (10)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x1B09)),
    ("Island Flyover - Progressive I-Point Group (11)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x1B0A)),
    ("Island Flyover - Progressive I-Point Group (12)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x1B0B)),
    ("Island Flyover - Progressive I-Point Group (13)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x1B0C)),
    ("Island Flyover - Progressive I-Point Group (14)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x1B0D)),
    ("Island Flyover - Progressive I-Point Group (15)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x1B0E)),
    ("Island Flyover - Progressive I-Point Group (16)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x1B0F)),
    ("Island Flyover - Progressive White Balloon Group (1)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B10)),
    ("Island Flyover - Progressive White Balloon Group (2)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B11)),
    ("Island Flyover - Progressive White Balloon Group (3)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B12)),
    ("Island Flyover - Progressive White Balloon Group (4)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B13)),
    ("Island Flyover - Progressive White Balloon Group (5)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B14)),
    ("Island Flyover - Progressive White Balloon Group (6)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B15)),
    ("Island Flyover - Progressive White Balloon Group (7)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B16)),
    ("Island Flyover - Progressive White Balloon Group (8)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B17)),
    ("Island Flyover - Progressive White Balloon Group (9)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x1B18)),
    ("Island Flyover - Progressive White Balloon Group (10)", LocData("Island Flyover", 'Custom',           12,             20,                     0x1B19)),
    ("Island Flyover - Progressive White Balloon Group (11)", LocData("Island Flyover", 'Custom',           12,             20,                     0x1B1A)),
    ("Island Flyover (Stamp) - Island Hopper",                LocData("Island Flyover", 'Stamp',            12,             20,                     0x0055)),
    ("Island Flyover (Stamp) - Pop Frenzy",                   LocData("Island Flyover", 'Hard Stamp',       12,             20,                     0x0056)),
    ("Island Flyover (Stamp) - Follow That Plane",            LocData("Island Flyover", 'Stamp',            12,             20,                     0x0057)),
    ("Island Flyover (Stamp) - Wuhu Tour Guide",              LocData("Island Flyover", 'Impossible Stamp', 12,             20,                     0x0058)),
    ("Island Flyover (Stamp) - Balloonatic",                  LocData("Island Flyover", 'Impossible Stamp', 12,             20,                     0x0059))
])                     

location_sort_order = {
    loc: i for i, loc in enumerate(location_table.keys())
}

location_groups = {
    'Stamp': [name for (name, data) in location_table.items() if data[0] == 'Stamp' or data[0] == 'Hard Stamp' or data[0] == 'Long Stamp' or data[0] == 'Impossible Stamp'],
    'Normal Stamp': [name for (name, data) in location_table.items() if data[0] == 'Stamp'],
    'Hard Stamp': [name for (name, data) in location_table.items() if data[0] == 'Hard Stamp'],
    'Impossible Stamp': [name for (name, data) in location_table.items() if data[0] == 'Impossible Stamp'],
    'Long Stamp': [name for (name, data) in location_table.items() if data[0] == 'Long Stamp'],
    'Pro Status': [name for (name, data) in location_table.items() if data[0] == 'Pro Status'],
    'Champion': [name for (name, data) in location_table.items() if data[0] == 'Champion'],
    'Difficulty': [name for (name, data) in location_table.items() if data[0] == 'Difficulty'],
    'iPoint': [name for (name, data) in location_table.items() if data[0] == 'iPoint'],
    'Custom': [name for (name, data) in location_table.items() if data[0] == 'Custom'],
}