from typing import Dict, TYPE_CHECKING
from .types import LocData
from .LocationList import location_table as lt

if TYPE_CHECKING:
    from . import WSRWorld

def get_total_locations(world: "WSRWorld") -> int:
    total = 0

    for name in location_table.keys():
        if is_location_valid(world, name):
            total += 1

    return total

def is_location_valid(world: "WSRWorld", location: str) -> bool:
    # this currently does absolutely nothing
    if world.options.sports_unlock_state == 0 and location in GLOBAL_LOCATIONS: #change to sports unlock list
        pass

    return True

def get_locations_names() -> Dict[str, int]:
    names = {name: data.id for name, data in lt.items()}
    return names


GLOBAL_LOCATIONS = {
    # None
}

# Swordplay Duel
SWF_VS_LOCATIONS = {
    "Swordplay Duel (Stamp) - Cliff-hanger": LocData("Duel", 0x0005, 1, 1),
    "Swordplay Duel (Stamp) - Straight to the Point": LocData("Duel", 0x0006, 1, 1),
    "Swordplay Duel (Stamp) - Met Your Match": LocData("Duel", 0x0007, 1, 1),
    "Swordplay Duel (Stamp) - One-Hit Wonder": LocData("Duel", 0x0008, 1, 1),
    "Swordplay Duel (Stamp) - Last Mii Standing": LocData("Duel", 0x0009, 1, 1),
    "Swordplay Duel - Pro Status": LocData("Duel", 0x1000, 1, 1),
    "Swordplay Duel - Beat The Champion (Matt)": LocData("Duel", 0x1001, 1, 1)
}

# Swordplay Speed Slice
SWF_PRC_LOCATIONS = {
    "Swordplay Speed Slice (Stamp) - Slice and Dice": LocData("Speed Slice", 0x000A, 1, 2),
    "Swordplay Speed Slice (Stamp) - Slicing Machine": LocData("Speed Slice", 0x000B, 1, 2),
    "Swordplay Speed Slice (Stamp) - Psychic Slice": LocData("Speed Slice", 0x000C, 1, 2),
    "Swordplay Speed Slice (Stamp) - Double Time": LocData("Speed Slice", 0x000D, 1, 2),
    "Swordplay Speed Slice (Stamp) - A Cut Above": LocData("Speed Slice", 0x000E, 1, 2),
    "Swordplay Speed Slice - Pro Status": LocData("Speed Slice", 0x1002, 1, 2),
    "Swordplay Speed Slice - Beat The Champion (Matt)": LocData("Speed Slice", 0x1003, 1, 2)
}

# Swordplay Showdown
SWF_SGL_LOCATIONS = {
    "Swordplay Showdown (Stamp) - Not a Scratch": LocData("Showdown Menu", 0x0000, 1, 3),
    "Swordplay Showdown (Stamp) - Sword Fighter": LocData("Volcano", 0x0001, 1, 3),
    "Swordplay Showdown (Stamp) - Perfect 10": LocData("Volcano", 0x0002, 1, 3),
    "Swordplay Showdown (Stamp) - Swordmaster": LocData("Volcano Reverse", 0x0003, 1, 3),
    "Swordplay Showdown (Stamp) - Untouchable": LocData("Volcano Reverse", 0x0004, 1, 3),
    "Swordplay Showdown - Complete Stage 1": LocData("Bridge", 0x1004, 1, 3),
    "Swordplay Showdown - Complete Stage 2": LocData("Showdown - Lighthouse", 0x1005, 1, 3),
    "Swordplay Showdown - Complete Stage 3": LocData("Showdown - Beach", 0x1006, 1, 3),
    "Swordplay Showdown - Complete Stage 4": LocData("Mountain", 0x1007, 1, 3),
    "Swordplay Showdown - Complete Stage 5": LocData("Forest", 0x1008, 1, 3),
    "Swordplay Showdown - Complete Stage 6": LocData("Ruins", 0x1009, 1, 3),
    "Swordplay Showdown - Complete Stage 7": LocData("Waterfall", 0x100A, 1, 3),
    "Swordplay Showdown - Complete Stage 8": LocData("Cliffs", 0x100B, 1, 3),
    "Swordplay Showdown - Complete Stage 9": LocData("Castle", 0x100C, 1, 3),
    "Swordplay Showdown - Complete Stage 10": LocData("Volcano", 0x100D, 1, 3),
    "Swordplay Showdown - Complete Stage 11": LocData("Bridge Reverse", 0x100E, 1, 3),
    "Swordplay Showdown - Complete Stage 12": LocData("Lighthouse Reverse", 0x100F, 1, 3),
    "Swordplay Showdown - Complete Stage 13": LocData("Beach Reverse", 0x1010, 1, 3),
    "Swordplay Showdown - Complete Stage 14": LocData("Mountain Reverse", 0x1011, 1, 3),
    "Swordplay Showdown - Complete Stage 15": LocData("Forest Reverse", 0x1012, 1, 3),
    "Swordplay Showdown - Complete Stage 16": LocData("Ruins Reverse", 0x1013, 1, 3),
    "Swordplay Showdown - Complete Stage 17": LocData("Waterfall Reverse", 0x1014, 1, 3),
    "Swordplay Showdown - Complete Stage 18": LocData("Cliffs Reverse", 0x1015, 1, 3),
    "Swordplay Showdown - Complete Stage 19": LocData("Castle Reverse", 0x1016, 1, 3),
    "Swordplay Showdown - Complete Stage 20": LocData("Volcano Reverse", 0x1017, 1, 3),
    "Swordplay Showdown - Pro Status": LocData("Showdown Menu", 0x1018, 1, 3),
}

# Wakeboarding
WKB_LOCATIONS = {
    "Wakeboarding (Stamp) - Huge Air": LocData("Wakeboarding Menu", 0x0050, 2, 4),
    "Wakeboarding (Stamp) - Bag of Tricks": LocData("Wakeboarding Menu", 0x0051, 2, 4),
    "Wakeboarding (Stamp) - Smooth Landing": LocData("Wakeboarding Menu", 0x0052, 2, 4),
    "Wakeboarding (Stamp) - Master Carver": LocData("Wakeboarding Menu", 0x0053, 2, 4),
    "Wakeboarding (Stamp) - The Long Way Home": LocData("Wakeboarding Menu", 0x0054, 2, 4),
    "Wakeboarding - Pro Status": LocData("Wakeboarding Menu", 0x1019, 2, 4)
}

# Frisbee Dog
FLD_LOCATIONS = {
    "Frisbee Dog (Stamp) - Good Dog": LocData("Frisbee Dog", 0x001E, 3, 5),
    "Frisbee Dog (Stamp) - Balloon Animal": LocData("Frisbee Dog", 0x001F, 3, 5),
    "Frisbee Dog (Stamp) - A for Effort": LocData("Frisbee Dog", 0x0020, 3, 5),
    "Frisbee Dog (Stamp) - Perfect Target": LocData("Frisbee Dog", 0x0021, 3, 5),
    "Frisbee Dog (Stamp) - Golden Arm": LocData("Frisbee Dog", 0x0022, 3, 5),
    "Frisbee Dog - Pro Status": LocData("Frisbee Dog", 0x101A, 3, 5)
}

# Frisbee Golf
DGL_LOCATIONS = {
    "Frisbee Golf (Stamp) - Under Par": LocData("Frisbee Golf Menu", 0x0064, 3, 6),
    "Frisbee Golf (Stamp) - Lucky Skip": LocData("Frisbee Golf Menu", 0x0065, 3, 6),
    "Frisbee Golf (Stamp) - On a Roll": LocData("Frisbee Golf Menu", 0x0066, 3, 6),
    "Frisbee Golf (Stamp) - Hole in One": LocData("Frisbee Golf Menu", 0x0067, 3, 6),
    "Frisbee Golf (Stamp) - Straight and Narrow": LocData("Frisbee Golf Menu", 0x0068, 3, 6),
    "Frisbee Golf - Complete Hole 1": LocData("Frisbee Golf Menu", 0x101B, 3, 6),
    "Frisbee Golf - Complete Hole 2": LocData("Frisbee Golf Menu", 0x101C, 3, 6),
    "Frisbee Golf - Complete Hole 3": LocData("Frisbee Golf Menu", 0x101D, 3, 6),
    "Frisbee Golf - Complete Hole 4": LocData("Frisbee Golf Menu", 0x101E, 3, 6),
    "Frisbee Golf - Complete Hole 5": LocData("Frisbee Golf Menu", 0x101F, 3, 6),
    "Frisbee Golf - Complete Hole 6": LocData("Frisbee Golf Menu", 0x1020, 3, 6),
    "Frisbee Golf - Complete Hole 7": LocData("Frisbee Golf Menu", 0x1021, 3, 6),
    "Frisbee Golf - Complete Hole 8": LocData("Frisbee Golf Menu", 0x1022, 3, 6),
    "Frisbee Golf - Complete Hole 9": LocData("Frisbee Golf Menu", 0x1023, 3, 6),
    "Frisbee Golf - Complete Hole 10": LocData("Frisbee Golf Menu", 0x1024, 3, 6),
    "Frisbee Golf - Complete Hole 11": LocData("Frisbee Golf Menu", 0x1025, 3, 6),
    "Frisbee Golf - Complete Hole 12": LocData("Frisbee Golf Menu", 0x1026, 3, 6),
    "Frisbee Golf - Complete Hole 13": LocData("Frisbee Golf Menu", 0x1027, 3, 6),
    "Frisbee Golf - Complete Hole 14": LocData("Frisbee Golf Menu", 0x1028, 3, 6),
    "Frisbee Golf - Complete Hole 15": LocData("Frisbee Golf Menu", 0x1029, 3, 6),
    "Frisbee Golf - Complete Hole 16": LocData("Frisbee Golf Menu", 0x102A, 3, 6),
    "Frisbee Golf - Complete Hole 17": LocData("Frisbee Golf Menu", 0x102B, 3, 6),
    "Frisbee Golf - Complete Hole 18": LocData("Frisbee Golf Menu", 0x102C, 3, 6),
    "Frisbee Golf - Complete Hole 19": LocData("Frisbee Golf Menu", 0x102D, 3, 6),
    "Frisbee Golf - Complete Hole 20": LocData("Frisbee Golf Menu", 0x102E, 3, 6),
    "Frisbee Golf - Complete Hole 21": LocData("Frisbee Golf Menu", 0x102F, 3, 6),
    "Frisbee Golf - Get a par": LocData("Frisbee Golf Menu", 0x1030, 3, 6),
    "Frisbee Golf - Get a birdie": LocData("Frisbee Golf Menu", 0x1031, 3, 6),
    "Frisbee Golf - Get an eagle": LocData("Frisbee Golf Menu", 0x1032, 3, 6),
    "Frisbee Golf - Pro Status": LocData("Frisbee Golf Menu", 0x1033, 3, 6)
}

# Archery
ARC_LOCATIONS = {
    "Archery (Stamp) - Bull Stampede": LocData("Archery", 0x0019, 4, 7),
    "Archery (Stamp) - Sure Shot": LocData("Archery", 0x001A, 4, 7),
    "Archery (Stamp) - Century Shot": LocData("Archery", 0x001B, 4, 7),
    "Archery (Stamp) - A Secret to Everybody": LocData("Archery", 0x001C, 4, 7),
    "Archery (Stamp) - Sharpshooter": LocData("Archery", 0x001D, 4, 7),
    "Archery - Pro Status": LocData("Archery", 0x1034, 4, 7)
}

# Basketball 3-Point Contest
BSK_3PT_LOCATIONS = {
    "3-Point Contest (Stamp) - Hot Streak": LocData("Basketball - 3 Point Contest", 0x0023, 5, 8),
    "3-Point Contest (Stamp) - Bonus Plumber": LocData("Basketball - 3 Point Contest", 0x0024, 5, 8),
    "3-Point Contest (Stamp) - Quick Draw": LocData("Basketball - 3 Point Contest", 0x0025, 5, 8),
    "3-Point Contest (Stamp) - Hot Hand": LocData("Basketball - 3 Point Contest", 0x0026, 5, 8),
    "3-Point Contest (Stamp) - Pure Shooter": LocData("Basketball - 3 Point Contest", 0x0027, 5, 8),
    "3-Point Contest - Pro Status": LocData("Basketball - 3 Point Contest", 0x1035, 5, 8)
}

# Basketball Pickup Game
BSK_VS_LOCATIONS = {
    "Pickup Game (Stamp) - Triple Dip": LocData("Basketball - Pickup Game", 0x0028, 5, 9),
    "Pickup Game (Stamp) - Rim Rattler": LocData("Basketball - Pickup Game", 0x0029, 5, 9),
    "Pickup Game (Stamp) - Lights Out": LocData("Basketball - Pickup Game", 0x002A, 5, 9),
    "Pickup Game (Stamp) - Buzzer Beater": LocData("Basketball - Pickup Game", 0x002B, 5, 9),
    "Pickup Game (Stamp) - Hoop Hero": LocData("Basketball - Pickup Game", 0x002C, 5, 9),
    "Pickup Game - Pro Status": LocData("Basketball - Pickup Game", 0x1036, 5, 9),
    "Pickup Game (Stamp) - Beat The Champion (Tommy)": LocData("Basketball - Pickup Game", 0x1037, 5, 9)
}

# Table Tennis Match
PNG_VS_LOCATIONS = {
    "Table Tennis Match (Stamp) - In Your Face": LocData("Table Tennis - Match", 0x004B, 6, 10),
    "Table Tennis Match (Stamp) - Back from the Brink": LocData("Table Tennis - Match", 0x004C, 6, 10),
    "Table Tennis Match (Stamp) - Epic Rally": LocData("Table Tennis - Match", 0x004D, 6, 10),
    "Table Tennis Match (Stamp) - Perfectly Matched": LocData("Table Tennis - Match", 0x004E, 6, 10),
    "Table Tennis Match (Stamp) - Table Titan": LocData("Table Tennis - Match", 0x004F, 6, 10),
    "Table Tennis Match - Pro Status": LocData("Table Tennis - Match", 0x1038, 6, 10),
    "Table Tennis Match - Beat The Champion (Lucia)": LocData("Table Tennis - Match", 0x1039, 6, 10),
}

# Table Tennis Return Challenge
PNG_RET_LOCATIONS = {
    "Return Challenge (Stamp) - 50-pointer": LocData("Table Tennis - Return Challenge", 0x0046, 6, 11),
    "Return Challenge (Stamp) - 100-pointer": LocData("Table Tennis - Return Challenge", 0x0047, 6, 11),
    "Return Challenge (Stamp) - 200-pointer": LocData("Table Tennis - Return Challenge", 0x0048, 6, 11),
    "Return Challenge (Stamp) - Recycler": LocData("Table Tennis - Return Challenge", 0x0049, 6, 11),
    "Return Challenge (Stamp) - Save Face": LocData("Table Tennis - Return Challenge", 0x004A, 6, 11),
    "Return Challenge - Pro Status": LocData("Table Tennis - Return Challenge", 0x103A, 6, 11)
}

# Golf
GLF_LOCATIONS = {
    "Golf (Stamp) - Under Par": LocData("Golf Menu", 0x005F, 7, 12),
    "Golf (Stamp) - Chip In": LocData("Golf Menu", 0x0060, 7, 12),
    "Golf (Stamp) - King of Clubs": LocData("Golf Menu", 0x0061, 7, 12),
    "Golf (Stamp) - Ace of Clubs": LocData("Golf Menu", 0x0062, 7, 12),
    "Golf (Stamp) - Hole in One": LocData("Golf Menu", 0x0063, 7, 12),
    "Golf - Complete Hole 1": LocData("Golf Menu", 0x103B, 7, 12),
    "Golf - Complete Hole 2": LocData("Golf Menu", 0x103C, 7, 12),
    "Golf - Complete Hole 3": LocData("Golf Menu", 0x103D, 7, 12),
    "Golf - Complete Hole 4": LocData("Golf Menu", 0x103E, 7, 12),
    "Golf - Complete Hole 5": LocData("Golf Menu", 0x103F, 7, 12),
    "Golf - Complete Hole 6": LocData("Golf Menu", 0x1040, 7, 12),
    "Golf - Complete Hole 7": LocData("Golf Menu", 0x1041, 7, 12),
    "Golf - Complete Hole 8": LocData("Golf Menu", 0x1042, 7, 12),
    "Golf - Complete Hole 9": LocData("Golf Menu", 0x1043, 7, 12),
    "Golf - Complete Hole 10": LocData("Golf Menu", 0x1044, 7, 12),
    "Golf - Complete Hole 11": LocData("Golf Menu", 0x1045, 7, 12),
    "Golf - Complete Hole 12": LocData("Golf Menu", 0x1046, 7, 12),
    "Golf - Complete Hole 13": LocData("Golf Menu", 0x1047, 7, 12),
    "Golf - Complete Hole 14": LocData("Golf Menu", 0x1048, 7, 12),
    "Golf - Complete Hole 15": LocData("Golf Menu", 0x1049, 7, 12),
    "Golf - Complete Hole 16": LocData("Golf Menu", 0x104A, 7, 12),
    "Golf - Complete Hole 17": LocData("Golf Menu", 0x104B, 7, 12),
    "Golf - Complete Hole 18": LocData("Golf Menu", 0x104C, 7, 12),
    "Golf - Complete Hole 19": LocData("Golf Menu", 0x104D, 7, 12),
    "Golf - Complete Hole 20": LocData("Golf Menu", 0x104E, 7, 12),
    "Golf - Complete Hole 21": LocData("Golf Menu", 0x104F, 7, 12),
    "Golf - Par": LocData("Golf Menu", 0x1050, 7, 12),
    "Golf - Birdie": LocData("Golf Menu", 0x1051, 7, 12),
    "Golf - Eagle": LocData("Golf Menu", 0x1052, 7, 12),
    "Golf - Pro Status": LocData("Golf Menu", 0x1053, 7, 12)
}

# Bowling 10-Pin Game
BWL_STD_LOCATIONS = {
    "Bowling Standard (Stamp) - Gobble Gobble": LocData("Bowling - Standard Game", 0x002D, 8, 13),
    "Bowling Standard (Stamp) - Split Spare": LocData("Bowling - Standard Game", 0x002E, 8, 13),
    "Bowling Standard (Stamp) - High Roller": LocData("Bowling - Standard Game", 0x002F, 8, 13),
    "Bowling Standard (Stamp) - Pin Dropper": LocData("Bowling - Standard Game", 0x0030, 8, 13),
    "Bowling Standard (Stamp) - Perfect Game": LocData("Bowling - Standard Game", 0x0031, 8, 13),
    "Bowling Standard - Pro Status": LocData("Bowling - Standard Game", 0x1054, 8, 13)
}

# Bowling 100-Pin Game
BWL_100_LOCATIONS = {
    "Bowling 100-Pin (Stamp) - Super Strike": LocData("Bowling - 100 Pin Game", 0x0032, 8, 14),
    "Bowling 100-Pin (Stamp) - Split Spare": LocData("Bowling - 100 Pin Game", 0x0033, 8, 14),
    "Bowling 100-Pin (Stamp) - Off the Wall": LocData("Bowling - 100 Pin Game", 0x0034, 8, 14),
    "Bowling 100-Pin (Stamp) - Secret Strike": LocData("Bowling - 100 Pin Game", 0x0035, 8, 14),
    "Bowling 100-Pin (Stamp) - Pin Dropper": LocData("Bowling - 100 Pin Game", 0x0036, 8, 14),
    "Bowling 100-Pin - Pro Status": LocData("Bowling - 100 Pin Game", 0x1055, 8, 14)
}

# Bowling Spin Control
BWL_WAL_LOCATIONS = {
    "Spin Control (Stamp) - One for All": LocData("Bowling - Spin Control", 0x0037, 8, 15),
    "Spin Control (Stamp) - Split Spare": LocData("Bowling - Spin Control", 0x0038, 8, 15),
    "Spin Control (Stamp) - Head First": LocData("Bowling - Spin Control", 0x0039, 8, 15),
    "Spin Control (Stamp) - English Major": LocData("Bowling - Spin Control", 0x003A, 8, 15),
    "Spin Control (Stamp) - Pin Dropper": LocData("Bowling - Spin Control", 0x003B, 8, 15),
    "Spin Control - Pro Status": LocData("Bowling - Spin Control", 0x1056, 8, 15)
}

# Power Cruising
JSK_LOCATIONS = {
    "Power Cruising (Stamp) - Ringmaster": LocData("Power Cruising Menu", 0x000F, 9, 16),
    "Power Cruising (Stamp) - 5,000-Pointer": LocData("Power Cruising Menu", 0x0010, 9, 16),
    "Power Cruising (Stamp) - Power Cruiser": LocData("Power Cruising Menu", 0x0011, 9, 16),
    "Power Cruising (Stamp) - Power Jumper": LocData("Power Cruising Menu", 0x0012, 9, 16),
    "Power Cruising (Stamp) - Leisure Cruiser": LocData("Power Cruising Menu", 0x0013, 9, 16),
    "Power Cruising - Pro Status": LocData("Power Cruising Menu", 0x1057, 9, 16)
}

# Canoeing
CAN_LOCATIONS = {
    "Canoeing (Stamp) - Beginner License": LocData("Canoeing Menu", 0x0041, 10, 17),
    "Canoeing (Stamp) - Intermediate License": LocData("Canoeing Menu", 0x0042, 10, 17),
    "Canoeing (Stamp) - Expert License": LocData("Canoeing Menu", 0x0043, 10, 17),
    "Canoeing (Stamp) - Ducks in a Row": LocData("Canoeing Menu", 0x0044, 10, 17),
    "Canoeing (Stamp) - Cut the Red Tape": LocData("Canoeing Menu", 0x0045, 10, 17),
    "Canoeing - Pro Status": LocData("Canoeing Menu", 0x1058, 10, 17)
}

# Cycling
BIC_LOCATIONS = {
    "Cycling (Stamp) - Last Gasp": LocData("Cycling Menu", 0x006E, 11, 18),
    "Cycling (Stamp) - First of Many": LocData("Cycling Menu", 0x006F, 11, 18),
    "Cycling (Stamp) - 1-Stage Master": LocData("Cycling Menu", 0x0070, 11, 18),
    "Cycling (Stamp) - 3-Stage Master": LocData("Cycling Menu", 0x0071, 11, 18),
    "Cycling (Stamp) - 6-Stage Master": LocData("Cycling Menu", 0x0072, 11, 18),
    "Cycling - Complete Stage 1": LocData("Around The Island", 0x1059, 11, 18),
    "Cycling - Complete Stage 2": LocData("To The Beach", 0x105A, 11, 18),
    "Cycling - Complete Stage 3": LocData("Across The Bridge", 0x105B, 11, 18),
    "Cycling - Complete Stage 4": LocData("Over Talon Rock", 0x105C, 11, 18),
    "Cycling - Complete Stage 5": LocData("Up The Volcano", 0x105D, 11, 18),
    "Cycling - Complete Stage 6": LocData("Into Maka Wuhu", 0x105E, 11, 18),
    "Cycling - Pro Status": LocData("Cycling Menu", 0x105F, 11, 18),
}

# Island Flyover
PLN_LOCATIONS = {
    "Skydiving (Stamp) - High Five": LocData("Skydiving", 0x0073, 12, 19),
    "Skydiving (Stamp) - For the Birds": LocData("Skydiving", 0x0074, 12, 19),
    "Skydiving (Stamp) - Friends in High Places": LocData("Skydiving", 0x0075, 12, 19),
    "Skydiving (Stamp) - Camera Shy": LocData("Skydiving", 0x0076, 12, 19),
    "Skydiving (Stamp) - 200-point Dive": LocData("Skydiving", 0x0077, 12, 19),
    "Skydiving - Pro Status": LocData("Skydiving", 0x1060, 12, 19)
}

# Skydiving
OMK_LOCATIONS = {
    "Island Flyover (Stamp) - Island Hopper": LocData("Island Flyover", 0x0055, 12, 20),
    "Island Flyover (Stamp) - Pop Frenzy": LocData("Island Flyover", 0x0056, 12, 20),
    "Island Flyover (Stamp) - Follow That Plane": LocData("Island Flyover", 0x0057, 12, 20),
    "Island Flyover (Stamp) - Wuhu Tour Guide": LocData("Island Flyover", 0x0058, 12, 20),
    "Island Flyover (Stamp) - Balloonatic": LocData("Island Flyover", 0x0059, 12, 20),
    "Island Flyover - Progressive I-Point Group (1)": LocData("Island Flyover", 0x1061, 12, 20),
    "Island Flyover - Progressive I-Point Group (2)": LocData("Island Flyover", 0x1062, 12, 20),
    "Island Flyover - Progressive I-Point Group (3)": LocData("Island Flyover", 0x1063, 12, 20),
    "Island Flyover - Progressive I-Point Group (4)": LocData("Island Flyover", 0x1064, 12, 20),
    "Island Flyover - Progressive I-Point Group (5)": LocData("Island Flyover", 0x1065, 12, 20),
    "Island Flyover - Progressive I-Point Group (6)": LocData("Island Flyover", 0x1066, 12, 20),
    "Island Flyover - Progressive I-Point Group (7)": LocData("Island Flyover", 0x1067, 12, 20),
    "Island Flyover - Progressive I-Point Group (8)": LocData("Island Flyover", 0x1068, 12, 20),
    "Island Flyover - Progressive I-Point Group (9)": LocData("Island Flyover", 0x1069, 12, 20),
    "Island Flyover - Progressive I-Point Group (10)": LocData("Island Flyover", 0x106A, 12, 20),
    "Island Flyover - Progressive I-Point Group (11)": LocData("Island Flyover", 0x106B, 12, 20),
    "Island Flyover - Progressive I-Point Group (12)": LocData("Island Flyover", 0x106C, 12, 20),
    "Island Flyover - Progressive I-Point Group (13)": LocData("Island Flyover", 0x106D, 12, 20),
    "Island Flyover - Progressive I-Point Group (14)": LocData("Island Flyover", 0x106E, 12, 20),
    "Island Flyover - Progressive I-Point Group (15)": LocData("Island Flyover", 0x106F, 12, 20),
    "Island Flyover - Progressive White Balloon Group (1)": LocData("Island Flyover", 0x1070, 12, 20),
    "Island Flyover - Progressive White Balloon Group (2)": LocData("Island Flyover", 0x1071, 12, 20),
    "Island Flyover - Progressive White Balloon Group (3)": LocData("Island Flyover", 0x1072, 12, 20),
    "Island Flyover - Progressive White Balloon Group (4)": LocData("Island Flyover", 0x1073, 12, 20),
    "Island Flyover - Progressive White Balloon Group (5)": LocData("Island Flyover", 0x1074, 12, 20),
    "Island Flyover - Progressive White Balloon Group (6)": LocData("Island Flyover", 0x1075, 12, 20),
    "Island Flyover - Progressive White Balloon Group (7)": LocData("Island Flyover", 0x1076, 12, 20),
    "Island Flyover - Progressive White Balloon Group (8)": LocData("Island Flyover", 0x1077, 12, 20),
    "Island Flyover - Progressive White Balloon Group (9)": LocData("Island Flyover", 0x1078, 12, 20),
    "Island Flyover - Progressive White Balloon Group (10)": LocData("Island Flyover", 0x1079, 12, 20),
    "Island Flyover - Progressive White Balloon Group (11)": LocData("Island Flyover", 0x107A, 12, 20)
}

HARD_STAMPS_LOCATIONS = {
    "Swordplay Showdown (Stamp) - Perfect 10": LocData("Volcano", 0x0002, 1, 3)
    # "Frisbee Dog (Stamp) - A for Effort": LocData("Frisbee Dog", 0, 3, 5),
    # "Frisbee Dog (Stamp) - Perfect Target": LocData("Frisbee Dog", 0, 3, 5),
    # "Frisbee Dog (Stamp) - Golden Arm": LocData("Frisbee Dog", 0, 3, 5),
    # "Frisbee Golf (Stamp) - On a Roll": LocData("Frisbee Golf Menu", 0, 3, 6),
    # "Archery (Stamp) - A Secret to Everybody": LocData("Archery", 0, 4, 7),
    # "3-Point Contest (Stamp) - Quick Draw": LocData("Basketball - 3 Point Contest", 0, 5, 8),
    # "Pickup Game (Stamp) - Lights Out": LocData("Basketball - Pickup Game", 0, 5, 9),
    # "Pickup Game (Stamp) - Buzzer Beater": LocData("Basketball - Pickup Game", 0, 5, 9),
    # "Table Tennis Match (Stamp) - Back from the Brink": LocData("Table Tennis - Match", 0, 6, 10),
    # "Table Tennis Match (Stamp) - Epic Rally": LocData("Table Tennis - Match", 0, 6, 10),
    # "Table Tennis Match (Stamp) - Perfectly Matched": LocData("Table Tennis - Match", 0, 6, 10),
    # "Return Challenge (Stamp) - 100-pointer": LocData("Table Tennis - Return Challenge", 0, 6, 11),
    # "Golf (Stamp) - King of Clubs": LocData("Golf Menu", 0, 7, 12),
    # "Bowling Standard (Stamp) - High Roller": LocData("Bowling - Standard Game", 0, 8, 13),
    # "Bowling Standard (Stamp) - Pin Dropper": LocData("Bowling - Standard Game", 0, 8, 13),
    # "Bowling 100-Pin (Stamp) - Pin Dropper": LocData("Bowling - 100 Pin Game", 0, 8, 14),
    # "Spin Control (Stamp) - English Major": LocData("Bowling - Spin Control", 0, 8, 15),
    # "Spin Control (Stamp) - Pin Dropper": LocData("Bowling - Spin Control", 0, 8, 15),
    # "Power Cruising (Stamp) - Power Cruiser": LocData("Power Cruising Menu", 0, 9, 16),
    # "Canoeing (Stamp) - Intermediate License": LocData("Canoeing Menu", 0, 10, 17),
    # "Skydiving (Stamp) - For the Birds": LocData("Skydiving", 0, 12, 19),
    # "Skydiving (Stamp) - 200-point Dive": LocData("Skydiving", 0, 12, 19),
    # "Island Flyover (Stamp) - Pop Frenzy": LocData("Island Flyover", 0, 12, 20) 
}

LONG_STAMPS_LOCATIONS = {
    "Swordplay Duel (Stamp) - Last Mii Standing": LocData("Duel", 0x0009, 1, 1)
    # "Swordplay Speed Slice (Stamp) - A Cut Above": LocData("Speed Slice", 0, 1, 2),
    # "Swordplay Showdown (Stamp) - Untouchable": LocData("Volcano Reverse", 0, 1, 3),
    # "Frisbee Golf (Stamp) - Straight and Narrow": LocData("Frisbee Golf Menu", 0, 3, 6),
    # "Archery (Stamp) - Sharpshooter": LocData("Archery", 0, 4, 7),
    # "3-Point Contest (Stamp) - Hot Hand": LocData("Basketball - 3 Point Contest", 0, 5, 8),
    # "3-Point Contest (Stamp) - Pure Shooter": LocData("Basketball - 3 Point Contest", 0, 5, 8),
    # "Pickup Game (Stamp) - Hoop Hero": LocData("Basketball - Pickup Game", 0, 5, 9),
    # "Table Tennis Match (Stamp) - Table Titan": LocData("Table Tennis - Match", 0, 6, 10),
    # "Return Challenge (Stamp) - 200-pointer": LocData("Table Tennis - Return Challenge", 0, 6, 11),
    # "Return Challenge (Stamp) - Recycler": LocData("Table Tennis - Return Challenge", 0, 6, 11),
    # "Return Challenge (Stamp) - Save Face": LocData("Table Tennis - Return Challenge", 0, 6, 11),
    # "Golf (Stamp) - Ace of Clubs": LocData("Golf Menu", 0, 7, 12),
    # "Golf (Stamp) - Hole in One": LocData("Golf Menu", 0, 7, 12),
    # "Bowling Standard (Stamp) - Perfect Game": LocData("Bowling - Standard Game", 0, 8, 13),
    # "Canoeing (Stamp) - Expert License": LocData("Canoeing Menu", 0, 10, 17),
    # "Canoeing (Stamp) - Cut the Red Tape": LocData("Canoeing Menu", 0, 10, 17),
    # "Island Flyover (Stamp) - Wuhu Tour Guide": LocData("Island Flyover", 0, 12, 20),
    # "Island Flyover (Stamp) - Balloonatic": LocData("Island Flyover", 0, 12, 20)
}

location_table = {
    **GLOBAL_LOCATIONS,
    **SWF_VS_LOCATIONS,
    **SWF_PRC_LOCATIONS,
    **SWF_SGL_LOCATIONS,
    **WKB_LOCATIONS,
    **FLD_LOCATIONS,
    **DGL_LOCATIONS,
    **ARC_LOCATIONS,
    **BSK_3PT_LOCATIONS,
    **BSK_VS_LOCATIONS,
    **PNG_VS_LOCATIONS,
    **PNG_RET_LOCATIONS,
    **GLF_LOCATIONS,
    **BWL_STD_LOCATIONS,
    **BWL_100_LOCATIONS,
    **BWL_WAL_LOCATIONS,
    **JSK_LOCATIONS,
    **CAN_LOCATIONS,
    **BIC_LOCATIONS,
    **PLN_LOCATIONS,
    **OMK_LOCATIONS
}