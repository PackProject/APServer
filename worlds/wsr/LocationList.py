from collections import OrderedDict
from typing import NamedTuple

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


#       Location:                                             Type                 Category ID    Sport ID                Location ID        
location_table = OrderedDict([
    #Swordplay Duel
    ("Swordplay Duel - First Win",                            LocData("Duel", 'Custom',            1,             1,                      0x0000)),
    ("Swordplay Duel (Stamp) - Cliff-hanger",                 LocData("Duel", 'Stamp',             1,             1,                      0x0001)),
    ("Swordplay Duel (Stamp) - Straight to the Point",        LocData("Duel", 'Stamp',             1,             1,                      0x0002)),
    ("Swordplay Duel (Stamp) - Met Your Match",               LocData("Duel", 'Stamp',             1,             1,                      0x0003)),
    ("Swordplay Duel (Stamp) - One-Hit Wonder",               LocData("Duel", 'Stamp',             1,             1,                      0x0004)),
    ("Swordplay Duel (Stamp) - Last Mii Standing",            LocData("Duel", 'Impossible Stamp',  1,             1,                      0x0005)),
    ("Swordplay Duel - Pro Status",                           LocData("Duel", 'Pro Status',        1,             1,                      0x0006)),
    ("Swordplay Duel - Beat The Champion (Matt)",             LocData("Duel", 'Champion',          1,             1,                      0x0007)), 
    #Swordplay Speed Slice
    ("Swordplay Speed Slice - First Win",                     LocData("Speed Slice", 'Custom',            1,             2,                      0x0008)),
    ("Swordplay Speed Slice (Stamp) - Slice and Dice",        LocData("Speed Slice", 'Stamp',             1,             2,                      0x0009)),
    ("Swordplay Speed Slice (Stamp) - Slicing Machine",       LocData("Speed Slice", 'Stamp',             1,             2,                      0x000A)),
    ("Swordplay Speed Slice (Stamp) - Psychic Slice",         LocData("Speed Slice", 'Stamp',             1,             2,                      0x000B)),
    ("Swordplay Speed Slice (Stamp) - Double Time",           LocData("Speed Slice", 'Stamp',             1,             2,                      0x000C)),
    ("Swordplay Speed Slice (Stamp) - A Cut Above",           LocData("Speed Slice", 'Impossible Stamp',  1,             2,                      0x000D)),
    ("Swordplay Speed Slice - Pro Status",                    LocData("Speed Slice", 'Pro Status',        1,             2,                      0x000E)),
    ("Swordplay Speed Slice - Beat The Champion (Matt)",      LocData("Speed Slice", 'Champion',          1,             2,                      0x000F)),
    #Swordplay Showdown
    ("Swordplay Showdown - Complete Stage 1",                 LocData("Bridge", 'Custom',            1,             3,                      0x0010)),
    ("Swordplay Showdown - Complete Stage 2",                 LocData("Showdown - Lighthouse", 'Custom',            1,             3,                      0x0011)),
    ("Swordplay Showdown - Complete Stage 3",                 LocData("Showdown - Beach", 'Custom',            1,             3,                      0x0012)),
    ("Swordplay Showdown - Complete Stage 4",                 LocData("Mountain", 'Custom',            1,             3,                      0x0013)),
    ("Swordplay Showdown - Complete Stage 5",                 LocData("Forest", 'Custom',            1,             3,                      0x0014)),
    ("Swordplay Showdown - Complete Stage 6",                 LocData("Ruins", 'Custom',            1,             3,                      0x0015)),
    ("Swordplay Showdown - Complete Stage 7",                 LocData("Waterfall", 'Custom',            1,             3,                      0x0016)),
    ("Swordplay Showdown - Complete Stage 8",                 LocData("Cliffs", 'Custom',            1,             3,                      0x0017)),
    ("Swordplay Showdown - Complete Stage 9",                 LocData("Castle", 'Custom',            1,             3,                      0x0018)),
    ("Swordplay Showdown - Complete Stage 10",                LocData("Volcano", 'Custom',            1,             3,                      0x0019)),
    ("Swordplay Showdown - Complete Stage 11",                LocData("Bridge Reverse", 'Custom',            1,             3,                      0x001A)),
    ("Swordplay Showdown - Complete Stage 12",                LocData("Lighthouse Reverse", 'Custom',            1,             3,                      0x001B)),
    ("Swordplay Showdown - Complete Stage 13",                LocData("Beach Reverse", 'Custom',            1,             3,                      0x001C)),
    ("Swordplay Showdown - Complete Stage 14",                LocData("Mountain Reverse", 'Custom',            1,             3,                      0x001D)),
    ("Swordplay Showdown - Complete Stage 15",                LocData("Forest Reverse", 'Custom',            1,             3,                      0x001E)),
    ("Swordplay Showdown - Complete Stage 16",                LocData("Ruins Reverse", 'Custom',            1,             3,                      0x001F)),
    ("Swordplay Showdown - Complete Stage 17",                LocData("Waterfall Reverse", 'Custom',            1,             3,                      0x0020)),
    ("Swordplay Showdown - Complete Stage 18",                LocData("Cliffs Reverse", 'Custom',            1,             3,                      0x0021)),
    ("Swordplay Showdown - Complete Stage 19",                LocData("Castle Reverse", 'Custom',            1,             3,                      0x0022)),
    ("Swordplay Showdown - Complete Stage 20",                LocData("Volcano Reverse", 'Custom',            1,             3,                      0x0023)),
    ("Swordplay Showdown (Stamp) - Not a Scratch",            LocData("Showdown Menu", 'Stamp',             1,             3,                      0x0024)),
    ("Swordplay Showdown (Stamp) - Sword Fighter",            LocData("Volcano", 'Long Stamp',        1,             3,                      0x0025)),
    ("Swordplay Showdown (Stamp) - Perfect 10",               LocData("Volcano", 'Hard Stamp',        1,             3,                      0x0026)),
    ("Swordplay Showdown (Stamp) - Swordmaster",              LocData("Volcano Reverse", 'Long Stamp',        1,             3,                      0x0027)),
    ("Swordplay Showdown (Stamp) - Untouchable",              LocData("Volcano Reverse", 'Impossible Stamp',  1,             3,                      0x0028)),
    ("Swordplay Showdown - Pro Status",                       LocData("Showdown Menu", 'Pro Status',        1,             3,                      0x0029)),
    #Wakeboarding
    ("Wakeboarding (Stamp) - Huge Air",                       LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x002A)),
    ("Wakeboarding (Stamp) - Bag of Tricks",                  LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x002B)),
    ("Wakeboarding (Stamp) - Smooth Landing",                 LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x002C)),
    ("Wakeboarding (Stamp) - Master Carver",                  LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x002D)),
    ("Wakeboarding (Stamp) - The Long Way Home",              LocData("Wakeboarding Menu", 'Stamp',             2,             4,                      0x002E)),
    ("Wakeboarding - Pro Status",                             LocData("Wakeboarding Menu", 'Pro Status',        2,             4,                      0x002F)),
    #Frisbee Dog
    ("Frisbee Dog (Stamp) - Good Dog",                        LocData("Frisbee Dog", 'Stamp',             3,             5,                      0x0030)),
    ("Frisbee Dog (Stamp) - Balloon Animal",                  LocData("Frisbee Dog", 'Stamp',             3,             5,                      0x0031)),
    ("Frisbee Dog (Stamp) - A for Effort",                    LocData("Frisbee Dog", 'Hard Stamp',        3,             5,                      0x0032)),
    ("Frisbee Dog (Stamp) - Perfect Target",                  LocData("Frisbee Dog", 'Hard Stamp',        3,             5,                      0x0033)),
    ("Frisbee Dog (Stamp) - Golden Arm",                      LocData("Frisbee Dog", 'Hard Stamp',        3,             5,                      0x0034)),
    ("Frisbee Dog - Pro Status",                              LocData("Frisbee Dog", 'Pro Status',        3,             5,                      0x0035)),
    #Frisbee Golf
    ("Frisbee Golf - Complete Hole 1",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0036)),
    ("Frisbee Golf - Complete Hole 2",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0037)),
    ("Frisbee Golf - Complete Hole 3",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0038)),
    ("Frisbee Golf - Complete Hole 4",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0039)),
    ("Frisbee Golf - Complete Hole 5",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x003A)),
    ("Frisbee Golf - Complete Hole 6",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x003B)),
    ("Frisbee Golf - Complete Hole 7",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x003C)),
    ("Frisbee Golf - Complete Hole 8",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x003D)),
    ("Frisbee Golf - Complete Hole 9",                        LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x003E)),
    ("Frisbee Golf - Complete Hole 10",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x003F)),
    ("Frisbee Golf - Complete Hole 11",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0040)),
    ("Frisbee Golf - Complete Hole 12",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0041)),
    ("Frisbee Golf - Complete Hole 13",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0042)),
    ("Frisbee Golf - Complete Hole 14",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0043)),
    ("Frisbee Golf - Complete Hole 15",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0044)),
    ("Frisbee Golf - Complete Hole 16",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0045)),
    ("Frisbee Golf - Complete Hole 17",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0046)),
    ("Frisbee Golf - Complete Hole 18",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0047)),
    ("Frisbee Golf - Complete Hole 19",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0048)),
    ("Frisbee Golf - Complete Hole 20",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x0049)),
    ("Frisbee Golf - Complete Hole 21",                       LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x004A)),            
    ("Frisbee Golf - Get a par",                              LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x004B)),
    ("Frisbee Golf - Get a birdie",                           LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x004C)),
    ("Frisbee Golf - Get an eagle",                           LocData("Frisbee Golf Menu", 'Custom',            3,             6,                      0x004D)),
    ("Frisbee Golf (Stamp) - Under Par",                      LocData("Frisbee Golf Menu", 'Stamp',             3,             6,                      0x004E)),
    ("Frisbee Golf (Stamp) - Lucky Skip",                     LocData("Frisbee Golf Menu", 'Stamp',             3,             6,                      0x004F)),
    ("Frisbee Golf (Stamp) - On a Roll",                      LocData("Frisbee Golf Menu", 'Hard Stamp',        3,             6,                      0x0050)),
    ("Frisbee Golf (Stamp) - Hole in One",                    LocData("Frisbee Golf Menu", 'Stamp',             3,             6,                      0x0051)),
    ("Frisbee Golf (Stamp) - Straight and Narrow",            LocData("Frisbee Golf Menu", 'Impossible Stamp',  3,             6,                      0x0052)),
    ("Frisbee Golf - Pro Status",                             LocData("Frisbee Golf Menu", 'Pro Status',        3,             6,                      0x0053)), 
    #Archery
    ("Archery (Stamp) - Bull Stampede",                       LocData("Archery", 'Stamp',             4,             7,                      0x0054)),
    ("Archery (Stamp) - Sure Shot",                           LocData("Archery", 'Stamp',             4,             7,                      0x0055)),
    ("Archery (Stamp) - Century Shot",                        LocData("Archery", 'Long Stamp',        4,             7,                      0x0056)),
    ("Archery (Stamp) - A Secret to Everybody",               LocData("Archery", 'Hard Stamp',        4,             7,                      0x0057)),
    ("Archery (Stamp) - Sharpshooter",                        LocData("Archery", 'Impossible Stamp',  4,             7,                      0x0058)),
    ("Archery - Pro Status",                                  LocData("Archery", 'Pro Status',        4,             7,                      0x0059)),
    #Basketball 3-Point Contest
    ("3-Point Contest (Stamp) - Hot Streak",                  LocData("Basketball - 3 Point Contest", 'Stamp',             5,             8,                      0x005A)),
    ("3-Point Contest (Stamp) - Bonus Plumber",               LocData("Basketball - 3 Point Contest", 'Stamp',             5,             8,                      0x005B)),
    ("3-Point Contest (Stamp) - Quick Draw",                  LocData("Basketball - 3 Point Contest", 'Hard Stamp',        5,             8,                      0x005C)),
    ("3-Point Contest (Stamp) - Hot Hand",                    LocData("Basketball - 3 Point Contest", 'Impossible Stamp',  5,             8,                      0x005D)),
    ("3-Point Contest (Stamp) - Pure Shooter",                LocData("Basketball - 3 Point Contest", 'Impossible Stamp',  5,             8,                      0x005E)),
    ("3-Point Contest - Pro Status",                          LocData("Basketball - 3 Point Contest", 'Pro Status',        5,             8,                      0x005F)),
    #Basketball Pickup Game
    ("Pickup Game (Stamp) - Triple Dip",                      LocData("Basketball - Pickup Game", 'Stamp',             5,             9,                      0x0060)),
    ("Pickup Game (Stamp) - Rim Rattler",                     LocData("Basketball - Pickup Game", 'Stamp',             5,             9,                      0x0061)),
    ("Pickup Game (Stamp) - Lights Out",                      LocData("Basketball - Pickup Game", 'Hard Stamp',        5,             9,                      0x0062)),
    ("Pickup Game (Stamp) - Buzzer Beater",                   LocData("Basketball - Pickup Game", 'Hard Stamp',        5,             9,                      0x0063)),
    ("Pickup Game (Stamp) - Hoop Hero",                       LocData("Basketball - Pickup Game", 'Impossible Stamp',  5,             9,                      0x0064)),
    ("Pickup Game - Pro Status",                              LocData("Basketball - Pickup Game", 'Pro Status',        5,             9,                      0x0065)),
    ("Pickup Game (Stamp) - Beat The Champion (Tommy)",       LocData("Basketball - Pickup Game", 'Champion',          5,             9,                      0x0066)),
    #Table Tennis
    ("Table Tennis Match (Stamp) - In Your Face",             LocData("Table Tennis - Match", 'Stamp',             6,             10,                     0x0067)),
    ("Table Tennis Match (Stamp) - Back from the Brink",      LocData("Table Tennis - Match", 'Hard Stamp',        6,             10,                     0x0068)),
    ("Table Tennis Match (Stamp) - Epic Rally",               LocData("Table Tennis - Match", 'Hard Stamp',        6,             10,                     0x0069)),
    ("Table Tennis Match (Stamp) - Perfectly Matched",        LocData("Table Tennis - Match", 'Hard Stamp',        6,             10,                     0x006A)),
    ("Table Tennis Match (Stamp) - Table Titan",              LocData("Table Tennis - Match", 'Impossible Stamp',  6,             10,                     0x006B)),
    ("Table Tennis Match - Pro Status",                       LocData("Table Tennis - Match", 'Pro Status',        6,             10,                     0x006C)),
    ("Table Tennis Match - Beat The Champion (Lucia)",        LocData("Table Tennis - Match", 'Champion',          6,             10,                     0x006D)),
    #Table Tennis Return Challenge
    ("Return Challenge (Stamp) - 50-pointer",                 LocData("Table Tennis - Return Challenge", 'Stamp',             6,             11,                     0x006E)),
    ("Return Challenge (Stamp) - 100-pointer",                LocData("Table Tennis - Return Challenge", 'Hard Stamp',        6,             11,                     0x006F)),
    ("Return Challenge (Stamp) - 200-pointer",                LocData("Table Tennis - Return Challenge", 'Impossible Stamp',  6,             11,                     0x0070)),
    ("Return Challenge (Stamp) - Recycler",                   LocData("Table Tennis - Return Challenge", 'Impossible Stamp',  6,             11,                     0x0071)),
    ("Return Challenge (Stamp) - Save Face",                  LocData("Table Tennis - Return Challenge", 'Impossible Stamp',  6,             11,                     0x0072)),
    ("Return Challenge - Pro Status",                         LocData("Table Tennis - Return Challenge", 'Pro Status',        6,             11,                     0x0073)),
    #Golf
    ("Golf - Complete Hole 1",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x0074)),
    ("Golf - Complete Hole 2",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x0075)),
    ("Golf - Complete Hole 3",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x0076)),
    ("Golf - Complete Hole 4",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x0077)),
    ("Golf - Complete Hole 5",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x0078)),
    ("Golf - Complete Hole 6",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x0079)),
    ("Golf - Complete Hole 7",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x007A)),
    ("Golf - Complete Hole 8",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x007B)),
    ("Golf - Complete Hole 9",                                LocData("Golf Menu", 'Custom',            7,             12,                     0x007C)),
    ("Golf - Complete Hole 10",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x007D)),
    ("Golf - Complete Hole 11",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x007E)),
    ("Golf - Complete Hole 12",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x007F)),
    ("Golf - Complete Hole 13",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0080)),
    ("Golf - Complete Hole 14",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0081)),
    ("Golf - Complete Hole 15",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0082)),
    ("Golf - Complete Hole 16",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0083)),
    ("Golf - Complete Hole 17",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0084)),
    ("Golf - Complete Hole 18",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0085)),
    ("Golf - Complete Hole 19",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0086)),
    ("Golf - Complete Hole 20",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0087)),
    ("Golf - Complete Hole 21",                               LocData("Golf Menu", 'Custom',            7,             12,                     0x0088)),
    ("Golf - Par",                                            LocData("Golf Menu", 'Custom',            7,             12,                     0x0089)),
    ("Golf - Birdie",                                         LocData("Golf Menu", 'Custom',            7,             12,                     0x008A)),
    ("Golf - Eagle",                                          LocData("Golf Menu", 'Custom',            7,             12,                     0x008B)),
    ("Golf (Stamp) - Under Par",                              LocData("Golf Menu", 'Stamp',             7,             12,                     0x008C)),
    ("Golf (Stamp) - Chip In",                                LocData("Golf Menu", 'Stamp',             7,             12,                     0x008D)),
    ("Golf (Stamp) - King of Clubs",                          LocData("Golf Menu", 'Hard Stamp',        7,             12,                     0x008E)),
    ("Golf (Stamp) - Ace of Clubs",                           LocData("Golf Menu", 'Impossible Stamp',  7,             12,                     0x008F)),
    ("Golf (Stamp) - Hole in One",                            LocData("Golf Menu", 'Impossible Stamp',  7,             12,                     0x0090)),
    ("Golf - Pro Status",                                     LocData("Golf Menu", 'Pro Status',        7,             12,                     0x0091)),         
    #Bowling 10 Pin
    ("Bowling 10 Pin - First Strike",                         LocData("Bowling - Standard Game", 'Custom',            8,             13,                     0x0E00)),
    ("Bowling Standard (Stamp) - Gobble Gobble",              LocData("Bowling - Standard Game", 'Stamp',             8,             13,                     0x0093)),
    ("Bowling Standard (Stamp) - Split Spare",                LocData("Bowling - Standard Game", 'Stamp',             8,             13,                     0x0094)),
    ("Bowling Standard (Stamp) - High Roller",                LocData("Bowling - Standard Game", 'Hard Stamp',        8,             13,                     0x0095)),
    ("Bowling Standard (Stamp) - Pin Dropper",                LocData("Bowling - Standard Game", 'Hard Stamp',        8,             13,                     0x0096)),
    ("Bowling Standard (Stamp) - Perfect Game",               LocData("Bowling - Standard Game", 'Impossible Stamp',  8,             13,                     0x0097)),
    ("Bowling Standard - Pro Status",                         LocData("Bowling - Standard Game", 'Pro Status',        8,             13,                     0x0098)),      
    #Bowling 100 Pin
    ("Bowling 100-Pin - First Strike",                        LocData("Bowling - 100 Pin Game", 'Custom',            8,             14,                     0x0099)),
    ("Bowling 100-Pin (Stamp) - Super Strike",                LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x009A)),
    ("Bowling 100-Pin (Stamp) - Split Spare",                 LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x009B)),
    ("Bowling 100-Pin (Stamp) - Off the Wall",                LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x009C)),
    ("Bowling 100-Pin (Stamp) - Secret Strike",               LocData("Bowling - 100 Pin Game", 'Stamp',             8,             14,                     0x009D)),
    ("Bowling 100-Pin (Stamp) - Pin Dropper",                 LocData("Bowling - 100 Pin Game", 'Hard Stamp',        8,             14,                     0x009E)),
    ("Bowling 100-Pin - Pro Status",                          LocData("Bowling - 100 Pin Game", 'Pro Status',        8,             14,                     0x009F)),
    #Bowling Spin Control
    ("Spin Control - First Strike",                           LocData("Bowling - Spin Control", 'Custom',            8,             15,                     0x00A0)),
    ("Spin Control (Stamp) - One for All",                    LocData("Bowling - Spin Control", 'Stamp',             8,             15,                     0x00A1)),
    ("Spin Control (Stamp) - Split Spare",                    LocData("Bowling - Spin Control", 'Stamp',             8,             15,                     0x00A2)),
    ("Spin Control (Stamp) - Head First",                     LocData("Bowling - Spin Control", 'Stamp',             8,             15,                     0x00A3)),
    ("Spin Control (Stamp) - English Major",                  LocData("Bowling - Spin Control", 'Hard Stamp',        8,             15,                     0x00A4)),
    ("Spin Control (Stamp) - Pin Dropper",                    LocData("Bowling - Spin Control", 'Hard Stamp',        8,             15,                     0x00A5)),
    ("Spin Control - Pro Status",                             LocData("Bowling - Spin Control", 'Pro Status',        8,             15,                     0x00A6)),     
    #Power Cruising
    ("Power Cruising (Stamp) - Ringmaster",                   LocData("Power Cruising Menu", 'Stamp',             9,             16,                     0x00A7)),
    ("Power Cruising (Stamp) - 5,000-Pointer",                LocData("Power Cruising Menu", 'Long Stamp',        9,             16,                     0x00A8)),
    ("Power Cruising (Stamp) - Power Cruiser",                LocData("Power Cruising Menu", 'Hard Stamp',        9,             16,                     0x00A9)),
    ("Power Cruising (Stamp) - Power Jumper",                 LocData("Power Cruising Menu", 'Stamp',             9,             16,                     0x00AA)),
    ("Power Cruising (Stamp) - Leisure Cruiser",              LocData("Power Cruising Menu", 'Long Stamp',        9,             16,                     0x00AB)),
    ("Power Cruising - Pro Status",                           LocData("Power Cruising Menu", 'Pro Status',        9,             16,                     0x00AC)),
    #Canoeing
    ("Canoeing (Stamp) - Beginner License",                   LocData("Canoeing Menu", 'Stamp',            10,             17,                     0x00AD)),
    ("Canoeing (Stamp) - Intermediate License",               LocData("Canoeing Menu", 'Hard Stamp',       10,             17,                     0x00AE)),
    ("Canoeing (Stamp) - Expert License",                     LocData("Canoeing Menu", 'Impossible Stamp', 10,             17,                     0x00AF)),
    ("Canoeing (Stamp) - Ducks in a Row",                     LocData("Canoeing Menu", 'Stamp',            10,             17,                     0x00B0)),
    ("Canoeing (Stamp) - Cut the Red Tape",                   LocData("Canoeing Menu", 'Impossible Stamp', 10,             17,                     0x00B1)),
    ("Canoeing - Pro Status",                                 LocData("Canoeing Menu", 'Pro Status',       10,             17,                     0x00B2)),
    #Cycling
    ("Cycling - Complete Stage 1",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x00B3)),
    ("Cycling - Complete Stage 2",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x00B4)),
    ("Cycling - Complete Stage 3",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x00B5)),
    ("Cycling - Complete Stage 4",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x00B6)),
    ("Cycling - Complete Stage 5",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x00B7)),
    ("Cycling - Complete Stage 6",                            LocData("Cycling Menu", 'Custom',           11,             18,                     0x00B8)),
    ("Cycling (Stamp) - Last Gasp",                           LocData("Cycling Menu", 'Stamp',            11,             18,                     0x00B9)),
    ("Cycling (Stamp) - First of Many",                       LocData("Cycling Menu", 'Stamp',            11,             18,                     0x00BA)),
    ("Cycling (Stamp) - 1-Stage Master",                      LocData("Cycling Menu", 'Long Stamp',       11,             18,                     0x00BB)),
    ("Cycling (Stamp) - 3-Stage Master",                      LocData("Cycling Menu", 'Long Stamp',       11,             18,                     0x00BC)),
    ("Cycling (Stamp) - 6-Stage Master",                      LocData("Cycling Menu", 'Long Stamp',       11,             18,                     0x00BD)),
    ("Cycling - Pro Status",                                  LocData("Cycling Menu", 'Pro Status',       11,             18,                     0x00BE)),
    #Skydiving
    ("Skydiving (Stamp) - High Five",                         LocData("Skydiving", 'Stamp',            12,             19,                     0x00BF)),
    ("Skydiving (Stamp) - For the Birds",                     LocData("Skydiving", 'Hard Stamp',       12,             19,                     0x00C0)),
    ("Skydiving (Stamp) - Friends in High Places",            LocData("Skydiving", 'Stamp',            12,             19,                     0x00C1)),
    ("Skydiving (Stamp) - Camera Shy",                        LocData("Skydiving", 'Stamp',            12,             19,                     0x00C2)),
    ("Skydiving (Stamp) - 200-point Dive",                    LocData("Skydiving", 'Hard Stamp',       12,             19,                     0x00C3)),
    ("Skydiving - Pro Status",                                LocData("Skydiving", 'Pro Status',       12,             19,                     0x00C4)),
    #Island Flyover
    ("Island Flyover - Progressive I-Point Group (1)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00C5)),
    ("Island Flyover - Progressive I-Point Group (2)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00C6)),
    ("Island Flyover - Progressive I-Point Group (3)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00C7)),
    ("Island Flyover - Progressive I-Point Group (4)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00C8)),
    ("Island Flyover - Progressive I-Point Group (5)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00C9)),
    ("Island Flyover - Progressive I-Point Group (6)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00CA)),
    ("Island Flyover - Progressive I-Point Group (7)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00CB)),
    ("Island Flyover - Progressive I-Point Group (8)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00CC)),
    ("Island Flyover - Progressive I-Point Group (9)",        LocData("Island Flyover", 'Custom',           12,             20,                     0x00CD)),
    ("Island Flyover - Progressive I-Point Group (10)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x00CE)),
    ("Island Flyover - Progressive I-Point Group (11)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x00CF)),
    ("Island Flyover - Progressive I-Point Group (12)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x00D0)),
    ("Island Flyover - Progressive I-Point Group (13)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x00D1)),
    ("Island Flyover - Progressive I-Point Group (14)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x00D2)),
    ("Island Flyover - Progressive I-Point Group (15)",       LocData("Island Flyover", 'Custom',           12,             20,                     0x00D3)),
    ("Island Flyover - Progressive White Balloon Group (1)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00D4)),
    ("Island Flyover - Progressive White Balloon Group (2)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00D5)),
    ("Island Flyover - Progressive White Balloon Group (3)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00D6)),
    ("Island Flyover - Progressive White Balloon Group (4)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00D7)),
    ("Island Flyover - Progressive White Balloon Group (5)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00D8)),
    ("Island Flyover - Progressive White Balloon Group (6)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00D9)),
    ("Island Flyover - Progressive White Balloon Group (7)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00DA)),
    ("Island Flyover - Progressive White Balloon Group (8)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00DB)),
    ("Island Flyover - Progressive White Balloon Group (9)",  LocData("Island Flyover", 'Custom',           12,             20,                     0x00DC)),
    ("Island Flyover - Progressive White Balloon Group (10)", LocData("Island Flyover", 'Custom',           12,             20,                     0x00DD)),
    ("Island Flyover - Progressive White Balloon Group (11)", LocData("Island Flyover", 'Custom',           12,             20,                     0x00DE)),
    ("Island Flyover (Stamp) - Island Hopper",                LocData("Island Flyover", 'Stamp',            12,             20,                     0x00DF)),
    ("Island Flyover (Stamp) - Pop Frenzy",                   LocData("Island Flyover", 'Hard Stamp',       12,             20,                     0x00E0)),
    ("Island Flyover (Stamp) - Follow That Plane",            LocData("Island Flyover", 'Stamp',            12,             20,                     0x00E1)),
    ("Island Flyover (Stamp) - Wuhu Tour Guide",              LocData("Island Flyover", 'Impossible Stamp', 12,             20,                     0x00E2)),
    ("Island Flyover (Stamp) - Balloonatic",                  LocData("Island Flyover", 'Impossible Stamp', 12,             20,                     0x00E3))
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