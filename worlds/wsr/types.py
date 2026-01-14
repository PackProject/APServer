from enum import IntEnum
from typing import NamedTuple, Optional, List
from BaseClasses import Location, Item, ItemClassification
from dataclasses import dataclass

class WSRLocation(Location):
    game = "Wii Sports Resort"

class WSRItem(Item):
    game = "Wii Sports Resort"

class LocData(NamedTuple):
    region: str = None
    id: int = 0
    category: int = 0
    sport: int = 0

class CategoryIndex(IntEnum):
    MENU = 0
    SWORDPLAY = 1
    WAKEBOARD = 2
    FRISBEE = 3
    ARCHERY = 4
    BASKETBALL = 5
    TABLE = 6
    GOLF = 7
    BOWLING = 8
    CRUISING = 9
    CANOE = 10
    CYCLING = 11
    AIR = 12

class SportIndex(IntEnum):
    MENU = 0
    DUEL = 1
    SPEED = 2
    SHOWDOWN = 3
    WAKEBOARD = 4
    DOG = 5
    FGOLF = 6
    ARCHERY = 7
    THREE = 8
    PICKUP = 9
    RETURN = 10
    MATCH = 11
    GOLF = 12
    TEN = 13
    HUNDRED = 14
    SPIN = 15
    CRUISING = 16
    CANOE = 17
    CYCLING = 18
    SKYDIVING = 19
    FLYOVER = 20

class WSRItemData(NamedTuple):
    itemType: str
    classification: ItemClassification
    category: CategoryIndex
    sport: SportIndex
    item_id: Optional[int]

