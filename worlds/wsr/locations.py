from typing import Dict, TYPE_CHECKING
from .types import LocData

if TYPE_CHECKING:
    from . import WSRWorld

def get_total_locations(world: "WSRWorld") -> int:
    total = 0

    for name in location_table.keys():
        if is_location_valid(world, name):
            total += 1

    return total

def is_location_valid(world: "WSRWorld", location: str) -> bool:
    if world.options.sports_unlock_state == 0 and location in GLOBAL_LOCATIONS: #change to sports unlock list
        pass

    return True

def get_locations_names() -> Dict[str, int]:
    names = {name: data.id for name, data in location_table.items()}
    return names


GLOBAL_LOCATIONS = {
    # None
}

# Swordplay Duel
SWF_VS_LOCATIONS = {
    "Swordplay Duel (Stamp) - Cliff-hanger": LocData(0, 1, 1),
    "Swordplay Duel (Stamp) - Straight to the Point": LocData(0, 1, 1),
    "Swordplay Duel (Stamp) - Met Your Match": LocData(0, 1, 1),
    "Swordplay Duel (Stamp) - One-Hit Wonder": LocData(0, 1, 1),
    "Swordplay Duel (Stamp) - Last Mii Standing": LocData(0, 1, 1),
    "Swordplay Duel - Pro Status": LocData(0, 1, 1),
    "Swordplay Duel - Beat The Champion (Matt)": LocData(0, 1, 1)
}

# Swordplay Speed Slice
SWF_PRC_LOCATIONS = {
    "Swordplay Speed Slice (Stamp) - Slice and Dice": LocData(0, 1, 2),
    "Swordplay Speed Slice (Stamp) - Slicing Machine": LocData(0, 1, 2),
    "Swordplay Speed Slice (Stamp) - Psychic Slice": LocData(0, 1, 2),
    "Swordplay Speed Slice (Stamp) - Double Time": LocData(0, 1, 2),
    "Swordplay Speed Slice (Stamp) - A Cut Above": LocData(0, 1, 2),
    "Swordplay Speed Slice - Pro Status": LocData(0, 1, 2),
    "Swordplay Speed Slice - Beat The Champion (Matt)": LocData(0, 1, 2)
}

# Swordplay Showdown
SWF_SGL_LOCATIONS = {
    "Swordplay Showdown (Stamp) - Not a Scratch": LocData(0, 1, 3),
    "Swordplay Showdown (Stamp) - Sword Fighter": LocData(0, 1, 3),
    "Swordplay Showdown (Stamp) - Perfect 10": LocData(0, 1, 3),
    "Swordplay Showdown (Stamp) - Swordmaster": LocData(0, 1, 3),
    "Swordplay Showdown (Stamp) - Untouchable": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 1": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 2": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 3": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 4": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 5": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 6": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 7": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 8": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 9": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 10": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 11": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 12": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 13": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 14": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 15": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 16": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 17": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 18": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 19": LocData(0, 1, 3),
    "Swordplay Showdown - Complete Stage 20": LocData(0, 1, 3),
    "Swordplay Showdown - Pro Status": LocData(0, 1, 3),
}

# Wakeboarding
WKB_LOCATIONS = {
    "Wakeboarding (Stamp) - Huge Air": LocData(0, 2, 4),
    "Wakeboarding (Stamp) - Bag of Tricks": LocData(0, 2, 4),
    "Wakeboarding (Stamp) - Smooth Landing": LocData(0, 2, 4),
    "Wakeboarding (Stamp) - Master Carver": LocData(0, 2, 4),
    "Wakeboarding (Stamp) - The Long Way Home": LocData(0, 2, 4),
    "Wakeboarding - Pro Status": LocData(0, 2, 4)
}

# Frisbee Dog
FLD_LOCATIONS = {
    "Frisbee Dog (Stamp) - Good Dog": LocData(0, 3, 5),
    "Frisbee Dog (Stamp) - Balloon Animal": LocData(0, 3, 5),
    "Frisbee Dog (Stamp) - A for Effort": LocData(0, 3, 5),
    "Frisbee Dog (Stamp) - Perfect Target": LocData(0, 3, 5),
    "Frisbee Dog (Stamp) - Golden Arm": LocData(0, 3, 5),
    "Frisbee Dog - Pro Status": LocData(0, 3, 5)
}

# Frisbee Golf
DGL_LOCATIONS = {
    "Frisbee Golf (Stamp) - Under Par": LocData(0, 3, 6),
    "Frisbee Golf (Stamp) - Lucky Skip": LocData(0, 3, 6),
    "Frisbee Golf (Stamp) - On a Roll": LocData(0, 3, 6),
    "Frisbee Golf (Stamp) - Hole in One": LocData(0, 3, 6),
    "Frisbee Golf (Stamp) - Straight and Narrow": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 1": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 2": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 3": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 4": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 5": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 6": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 7": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 8": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 9": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 10": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 11": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 12": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 13": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 14": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 15": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 16": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 17": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 18": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 19": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 20": LocData(0, 3, 6),
    "Frisbee Golf - Complete Hole 21": LocData(0, 3, 6),
    "Frisbee Golf - Get a par": LocData(0, 3, 6),
    "Frisbee Golf - Get a birdie": LocData(0, 3, 6),
    "Frisbee Golf - Get an eagle": LocData(0, 3, 6),
    "Frisbee Golf - Pro Status": LocData(0, 3, 6)
}

# Archery
ARC_LOCATIONS = {
    "Archery (Stamp) - Bull Stampede": LocData(0, 4, 7),
    "Archery (Stamp) - Sure Shot": LocData(0, 4, 7),
    "Archery (Stamp) - Century Shot": LocData(0, 4, 7),
    "Archery (Stamp) - A Secret to Everybody": LocData(0, 4, 7),
    "Archery (Stamp) - Sharpshooter": LocData(0, 4, 7),
    "Archery - Pro Status": LocData(0, 4, 7)
}

# Basketball 3-Point Contest
BSK_3PT_LOCATIONS = {
    "3-Point Contest (Stamp) - Hot Streak": LocData(0, 5, 8),
    "3-Point Contest (Stamp) - Bonus Plumber": LocData(0, 5, 8),
    "3-Point Contest (Stamp) - Quick Draw": LocData(0, 5, 8),
    "3-Point Contest (Stamp) - Hot Hand": LocData(0, 5, 8),
    "3-Point Contest (Stamp) - Pure Shooter": LocData(0, 5, 8),
    "3-Point Contest - Pro Status": LocData(0, 5, 8)
}

# Basketball Pickup Game
BSK_VS_LOCATIONS = {
    "Pickup Game (Stamp) - Triple Dip": LocData(0, 5, 9),
    "Pickup Game (Stamp) - Rim Rattler": LocData(0, 5, 9),
    "Pickup Game (Stamp) - Lights Out": LocData(0, 5, 9),
    "Pickup Game (Stamp) - Buzzer Beater": LocData(0, 5, 9),
    "Pickup Game (Stamp) - Hoop Hero": LocData(0, 5, 9),
    "Pickup Game - Pro Status": LocData(0, 5, 9),
    "Pickup Game (Stamp) - Beat The Champion (Tommy)": LocData(0, 5, 9)
}

# Table Tennis Match
PNG_VS_LOCATIONS = {
    "Table Tennis Match (Stamp) - In Your Face": LocData(0, 6, 10),
    "Table Tennis Match (Stamp) - Back from the Brink": LocData(0, 6, 10),
    "Table Tennis Match (Stamp) - Epic Rally": LocData(0, 6, 10),
    "Table Tennis Match (Stamp) - Perfectly Matched": LocData(0, 6, 10),
    "Table Tennis Match (Stamp) - Table Titan": LocData(0, 6, 10),
    "Table Tennis Match - Pro Status": LocData(0, 6, 10),
    "Table Tennis Match - Beat The Champion (Lucia)": LocData(0, 6, 10),
}

# Table Tennis Return Challenge
PNG_RET_LOCATIONS = {
    "Return Challenge (Stamp) - 50-pointer": LocData(0, 6, 11),
    "Return Challenge (Stamp) - 100-pointer": LocData(0, 6, 11),
    "Return Challenge (Stamp) - 200-pointer": LocData(0, 6, 11),
    "Return Challenge (Stamp) - Recycler": LocData(0, 6, 11),
    "Return Challenge (Stamp) - Save Face": LocData(0, 6, 11),
    "Return Challenge - Pro Status": LocData(0, 6, 11)
}

# Golf
GLF_LOCATIONS = {
    "Golf (Stamp) - Under Par": LocData(0, 7, 12),
    "Golf (Stamp) - Chip In": LocData(0, 7, 12),
    "Golf (Stamp) - King of Clubs": LocData(0, 7, 12),
    "Golf (Stamp) - Ace of Clubs": LocData(0, 7, 12),
    "Golf (Stamp) - Hole in One": LocData(0, 7, 12),
    "Golf - Complete Hole 1": LocData(0, 7, 12),
    "Golf - Complete Hole 2": LocData(0, 7, 12),
    "Golf - Complete Hole 3": LocData(0, 7, 12),
    "Golf - Complete Hole 4": LocData(0, 7, 12),
    "Golf - Complete Hole 5": LocData(0, 7, 12),
    "Golf - Complete Hole 6": LocData(0, 7, 12),
    "Golf - Complete Hole 7": LocData(0, 7, 12),
    "Golf - Complete Hole 8": LocData(0, 7, 12),
    "Golf - Complete Hole 9": LocData(0, 7, 12),
    "Golf - Complete Hole 10": LocData(0, 7, 12),
    "Golf - Complete Hole 11": LocData(0, 7, 12),
    "Golf - Complete Hole 12": LocData(0, 7, 12),
    "Golf - Complete Hole 13": LocData(0, 7, 12),
    "Golf - Complete Hole 14": LocData(0, 7, 12),
    "Golf - Complete Hole 15": LocData(0, 7, 12),
    "Golf - Complete Hole 16": LocData(0, 7, 12),
    "Golf - Complete Hole 17": LocData(0, 7, 12),
    "Golf - Complete Hole 18": LocData(0, 7, 12),
    "Golf - Complete Hole 19": LocData(0, 7, 12),
    "Golf - Complete Hole 20": LocData(0, 7, 12),
    "Golf - Complete Hole 21": LocData(0, 7, 12),
    "Golf - Par": LocData(0, 7, 12),
    "Golf - Birdie": LocData(0, 7, 12),
    "Golf - Eagle": LocData(0, 7, 12),
    "Golf - Pro Status": LocData(0, 7, 12)
}

# Bowling 10-Pin Game
BWL_STD_LOCATIONS = {
    "Bowling Standard (Stamp) - Gobble Gobble": LocData(0, 8, 13),
    "Bowling Standard (Stamp) - Split Spare": LocData(0, 8, 13),
    "Bowling Standard (Stamp) - High Roller": LocData(0, 8, 13),
    "Bowling Standard (Stamp) - Pin Dropper": LocData(0, 8, 13),
    "Bowling Standard (Stamp) - Perfect Game": LocData(0, 8, 13),
    "Bowling Standard - Pro Status": LocData(0, 8, 13)
}

# Bowling 100-Pin Game
BWL_100_LOCATIONS = {
    "Bowling 100-Pin (Stamp) - Super Strike": LocData(0, 8, 14),
    "Bowling 100-Pin (Stamp) - Split Spare": LocData(0, 8, 14),
    "Bowling 100-Pin (Stamp) - Off the Wall": LocData(0, 8, 14),
    "Bowling 100-Pin (Stamp) - Secret Strike": LocData(0, 8, 14),
    "Bowling 100-Pin (Stamp) - Pin Dropper": LocData(0, 8, 14),
    "Bowling 100-Pin - Pro Status": LocData(0, 8, 14)
}

# Bowling Spin Control
BWL_WAL_LOCATIONS = {
    "Spin Control (Stamp) - One for All": LocData(0, 8, 15),
    "Spin Control (Stamp) - Split Spare": LocData(0, 8, 15),
    "Spin Control (Stamp) - Head First": LocData(0, 8, 15),
    "Spin Control (Stamp) - English Major": LocData(0, 8, 15),
    "Spin Control (Stamp) - Pin Dropper": LocData(0, 8, 15),
    "Spin Control - Pro Status": LocData(0, 8, 15)
}

# Power Cruising
JSK_LOCATIONS = {
    "Power Cruising (Stamp) - Ringmaster": LocData(0, 9, 16),
    "Power Cruising (Stamp) - 5,000-Pointer": LocData(0, 9, 16),
    "Power Cruising (Stamp) - Power Cruiser": LocData(0, 9, 16),
    "Power Cruising (Stamp) - Power Jumper": LocData(0, 9, 16),
    "Power Cruising (Stamp) - Leisure Cruiser": LocData(0, 9, 16),
    "Power Cruising - Pro Status": LocData(0, 9, 16)
}

# Canoeing
CAN_LOCATIONS = {
    "Canoeing (Stamp) - Beginner License": LocData(0, 10, 17),
    "Canoeing (Stamp) - Intermediate License": LocData(0, 10, 17),
    "Canoeing (Stamp) - Expert License": LocData(0, 10, 17),
    "Canoeing (Stamp) - Ducks in a Row": LocData(0, 10, 17),
    "Canoeing (Stamp) - Cut the Red Tape": LocData(0, 10, 17),
    "Canoeing - Pro Status": LocData(0, 10, 17)
}

# Cycling
BIC_LOCATIONS = {
    "Cycling (Stamp) - Last Gasp": LocData(0, 11, 18),
    "Cycling (Stamp) - First of Many": LocData(0, 11, 18),
    "Cycling (Stamp) - 1-Stage Master": LocData(0, 11, 18),
    "Cycling (Stamp) - 3-Stage Master": LocData(0, 11, 18),
    "Cycling (Stamp) - 6-Stage Master": LocData(0, 11, 18),
    "Cycling - Complete Stage 1": LocData(0, 11, 18),
    "Cycling - Complete Stage 2": LocData(0, 11, 18),
    "Cycling - Complete Stage 3": LocData(0, 11, 18),
    "Cycling - Complete Stage 4": LocData(0, 11, 18),
    "Cycling - Complete Stage 5": LocData(0, 11, 18),
    "Cycling - Complete Stage 6": LocData(0, 11, 18),
    "Cycling - Pro Status": LocData(0, 11, 18),
}

# Island Flyover
PLN_LOCATIONS = {
    "Skydiving (Stamp) - High Five": LocData(0, 12, 19),
    "Skydiving (Stamp) - For the Birds": LocData(0, 12, 19),
    "Skydiving (Stamp) - Friends in High Places": LocData(0, 12, 19),
    "Skydiving (Stamp) - Camera Shy": LocData(0, 12, 19),
    "Skydiving (Stamp) - 200-point Dive": LocData(0, 12, 19),
    "Skydiving - Pro Status": LocData(0, 12, 19)
}

# Skydiving
OMK_LOCATIONS = {
    "Island Flyover (Stamp) - Island Hopper": LocData(0, 12, 20),
    "Island Flyover (Stamp) - Pop Frenzy": LocData(0, 12, 20),
    "Island Flyover (Stamp) - Follow That Plane": LocData(0, 12, 20),
    "Island Flyover (Stamp) - Wuhu Tour Guide": LocData(0, 12, 20),
    "Island Flyover (Stamp) - Balloonatic": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (1)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (2)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (3)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (4)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (5)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (6)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (7)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (8)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (9)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (10)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (11)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (12)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (13)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (14)": LocData(0, 12, 20),
    "Island Flyover - Progressive I-Point Group (15)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (1)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (2)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (3)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (4)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (5)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (6)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (7)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (8)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (9)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (10)": LocData(0, 12, 20),
    "Island Flyover - Progressive White Balloon Group (11)": LocData(0, 12, 20)
}

HARD_STAMPS_LOCATIONS = {
    "Swordplay Showdown (Stamp) - Perfect 10": LocData(0, 1, 3),
    "Frisbee Dog (Stamp) - A for Effort": LocData(0, 3, 5),
    "Frisbee Dog (Stamp) - Perfect Target": LocData(0, 3, 5),
    "Frisbee Dog (Stamp) - Golden Arm": LocData(0, 3, 5),
    "Frisbee Golf (Stamp) - On a Roll": LocData(0, 3, 6),
    "Archery (Stamp) - A Secret to Everybody": LocData(0, 4, 7),
    "3-Point Contest (Stamp) - Quick Draw": LocData(0, 5, 8),
    "Pickup Game (Stamp) - Lights Out": LocData(0, 5, 9),
    "Pickup Game (Stamp) - Buzzer Beater": LocData(0, 5, 9),
    "Table Tennis Match (Stamp) - Back from the Brink": LocData(0, 6, 10),
    "Table Tennis Match (Stamp) - Epic Rally": LocData(0, 6, 10),
    "Table Tennis Match (Stamp) - Perfectly Matched": LocData(0, 6, 10),
    "Return Challenge (Stamp) - 100-pointer": LocData(0, 6, 11),
    "Golf (Stamp) - King of Clubs": LocData(0, 7, 12),
    "Bowling Standard (Stamp) - High Roller": LocData(0, 8, 13),
    "Bowling Standard (Stamp) - Pin Dropper": LocData(0, 8, 13),
    "Bowling 100-Pin (Stamp) - Pin Dropper": LocData(0, 8, 15),
    "Spin Control (Stamp) - English Major": LocData(0, 8, 15),
    "Spin Control (Stamp) - Pin Dropper": LocData(0, 8, 15),
    "Power Cruising (Stamp) - Power Cruiser": LocData(0, 9, 16),
    "Canoeing (Stamp) - Intermediate License": LocData(0, 10, 17),
    "Skydiving (Stamp) - For the Birds": LocData(0, 12, 19),
    "Skydiving (Stamp) - 200-point Dive": LocData(0, 12, 19),
    "Island Flyover (Stamp) - Pop Frenzy": LocData(0, 12, 20)
}

LONG_STAMPS_LOCATIONS = {
    "Swordplay Duel (Stamp) - Last Mii Standing": LocData(0, 1, 1),
    "Swordplay Speed Slice (Stamp) - A Cut Above": LocData(0, 1, 2),
    "Swordplay Showdown (Stamp) - Untouchable": LocData(0, 1, 3),
    "Frisbee Golf (Stamp) - Straight and Narrow": LocData(0, 3, 6),
    "Archery (Stamp) - Sharpshooter": LocData(0, 4, 7),
    "3-Point Contest (Stamp) - Hot Hand": LocData(0, 5, 8),
    "3-Point Contest (Stamp) - Pure Shooter": LocData(0, 5, 8),
    "Pickup Game (Stamp) - Hoop Hero": LocData(0, 5, 9),
    "Table Tennis Match (Stamp) - Table Titan": LocData(0, 6, 10),
    "Return Challenge (Stamp) - 200-pointer": LocData(0, 6, 11),
    "Return Challenge (Stamp) - Recycler": LocData(0, 6, 11),
    "Return Challenge (Stamp) - Save Face": LocData(0, 6, 11),
    "Golf (Stamp) - Ace of Clubs": LocData(0, 7, 12),
    "Golf (Stamp) - Hole in One": LocData(0, 7, 12),
    "Bowling Standard (Stamp) - Perfect Game": LocData(0, 8, 13),
    "Canoeing (Stamp) - Expert License": LocData(0, 10, 17),
    "Canoeing (Stamp) - Cut the Red Tape": LocData(0, 10, 17),
    "Island Flyover (Stamp) - Wuhu Tour Guide": LocData(0, 12, 20),
    "Island Flyover (Stamp) - Balloonatic": LocData(0, 12, 20)
}



location_table = {
    **GLOBAL_LOCATIONS
    **SWF_VS_LOCATIONS
    **SWF_PRC_LOCATIONS
    **SWF_SGL_LOCATIONS
    **WKB_LOCATIONS
    **FLD_LOCATIONS
    **DGL_LOCATIONS
    **ARC_LOCATIONS
    **BSK_3PT_LOCATIONS
    **BSK_VS_LOCATIONS
    **PNG_VS_LOCATIONS
    **PNG_RET_LOCATIONS
    **GLF_LOCATIONS
    **BWL_STD_LOCATIONS
    **BWL_100_LOCATIONS
    **BWL_WAL_LOCATIONS
    **JSK_LOCATIONS
    **CAN_LOCATIONS
    **BIC_LOCATIONS
    **PLN_LOCATIONS
    **OMK_LOCATIONS
}