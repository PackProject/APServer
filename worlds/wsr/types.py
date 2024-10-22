from enum import IntEnum
from typing import NamedTuple, Optional, List
from BaseClasses import Location, Item, ItemClassification

class WSRLocation(Location):
    game = "Wii Sports Resort"

class WSRItem(Item):
    game = "Wii Sports Resort"

class CategoryIndex(IntEnum):
    SWORDPLAY = 0
    WAKEBOARD = 1
    FRISBEE = 2
    ARCHERY = 3
    BASKETBALL = 4
    TABLE = 5
    GOLF = 6
    BOWLING = 7
    CRUISING = 8
    CANOE = 9
    CYCLING = 10
    AIR = 11

class SportIndex(IntEnum):
    DUEL = 0
    SPEED = 1
    SHOWDOWN = 2
    WAKEBOARD = 3
    DOG = 4
    FGOLF = 5
    ARCHERY = 6
    THREE = 7
    PICKUP = 8
    RETURN = 9
    MATCH = 10
    GOLF = 11
    TEN = 12
    HUNDRED = 13
    SPIN = 14
    CRUISING = 15
    CANOE = 16
    CYCLING = 17
    SKYDIVING = 18
    FLYOVER = 19