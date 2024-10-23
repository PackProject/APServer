from BaseClasses import Item
from BaseClasses import ItemClassification as ItemType
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import WSRWorld


class WSRItem(Item):
    game = "Wii Sports Resort"

def create_itempool(world: "WSRWorld") -> List[Item]:
    itempool: List[Item] = []
    



#
# Any item that prevents the player from earning a stamp should be classified
# as a progression item.
#

ITEM_LIST = [
# fmt: off
    WSRItem("Unlock Swordplay",                            ItemType.progression),
    WSRItem("Unlock Wakeboarding",                         ItemType.progression),
    WSRItem("Unlock Frisbee",                              ItemType.progression),
    WSRItem("Unlock Archery",                              ItemType.progression),
    WSRItem("Unlock Basketball",                           ItemType.progression),
    WSRItem("Unlock Table Tennis",                         ItemType.progression),
    WSRItem("Unlock Golf",                                 ItemType.progression),
    WSRItem("Unlock Bowling",                              ItemType.progression),
    WSRItem("Unlock Power Cruising",                       ItemType.progression),
    WSRItem("Unlock Canoeing",                             ItemType.progression),
    WSRItem("Unlock Cycling",                              ItemType.progression),
    WSRItem("Unlock Air Sports",                           ItemType.progression),

    WSRItem("Swordplay - Duel",                            ItemType.progression),
    WSRItem("Swordplay (Duel) - Blocking",                 ItemType.useful),

    WSRItem("Swordplay - Speed Slice",                     ItemType.progression),
    WSRItem("Swordplay (Speed Slice) - Pausing",           ItemType.useful),

    WSRItem("Swordplay - Showdown",                        ItemType.progression),
    WSRItem("Swordplay (Showdown) - Blocking",             ItemType.useful),
    WSRItem("Swordplay (Showdown) - Extra Max Heart",      ItemType.useful),
    WSRItem("Swordplay (Showdown) - Extra Max Heart",      ItemType.useful),
    WSRItem("Swordplay (Showdown) - Lighthouse",           ItemType.progression),
    WSRItem("Swordplay (Showdown) - Beach",                ItemType.progression),
    WSRItem("Swordplay (Showdown) - Mountain",             ItemType.progression),
    WSRItem("Swordplay (Showdown) - Forest",               ItemType.progression),
    WSRItem("Swordplay (Showdown) - Ruins",                ItemType.progression),
    WSRItem("Swordplay (Showdown) - Waterfall",            ItemType.progression),
    WSRItem("Swordplay (Showdown) - Cliffs",               ItemType.progression),
    WSRItem("Swordplay (Showdown) - Castle",               ItemType.progression),
    WSRItem("Swordplay (Showdown) - Volcano",              ItemType.progression),
    WSRItem("Swordplay (Showdown) - Bridge (Reverse)",     ItemType.progression),
    WSRItem("Swordplay (Showdown) - Lighthouse (Reverse)", ItemType.progression),
    WSRItem("Swordplay (Showdown) - Beach (Reverse)",      ItemType.progression),
    WSRItem("Swordplay (Showdown) - Mountain (Reverse)",   ItemType.progression),
    WSRItem("Swordplay (Showdown) - Forest (Reverse)",     ItemType.progression),
    WSRItem("Swordplay (Showdown) - Ruins (Reverse)",      ItemType.progression),
    WSRItem("Swordplay (Showdown) - Waterfall (Reverse)",  ItemType.progression),
    WSRItem("Swordplay (Showdown) - Cliffs (Reverse)",     ItemType.progression),
    WSRItem("Swordplay (Showdown) - Castle (Reverse)",     ItemType.progression),
    WSRItem("Swordplay (Showdown) - Volcano (Reverse)",    ItemType.progression),

    # TODO: How will this affect Free Cruising (max 5 min.)?
    WSRItem("Wakeboarding - Extra Max Time",               ItemType.progression),
    WSRItem("Wakeboarding - Extra Max Time",               ItemType.progression),
    WSRItem("Wakeboarding - Extra Max Time",               ItemType.progression),
    WSRItem("Wakeboarding - Extra Max Time",               ItemType.progression),
    WSRItem("Wakeboarding - Beginner",                     ItemType.progression),
    WSRItem("Wakeboarding - Intermediate",                 ItemType.progression),
    WSRItem("Wakeboarding - Expert",                       ItemType.progression),

    WSRItem("Frisbee - Frisbee Dog",                       ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - Extra Throw",                   ItemType.progression),
    WSRItem("Frisbee Dog - A+2 to Pop Balloons",           ItemType.useful),

    # TODO: Must progressive items share the same ID?
    WSRItem("Frisbee - Frisbee Golf",                      ItemType.progression),
    WSRItem("Frisbee Golf - Progressive Frisbee",          ItemType.progression),
    WSRItem("Frisbee Golf - Progressive Frisbee",          ItemType.progression),
    WSRItem("Frisbee Golf - Progressive Frisbee",          ItemType.progression),
    WSRItem("Frisbee Golf - Three Holes (Resort A)",       ItemType.progression),
    WSRItem("Frisbee Golf - Three Holes (Resort B)",       ItemType.progression),
    WSRItem("Frisbee Golf - Three Holes (Resort C)",       ItemType.progression),
    WSRItem("Frisbee Golf - Three Holes (Classic A)",      ItemType.progression),
    WSRItem("Frisbee Golf - Three Holes (Classic B)",      ItemType.progression),
    WSRItem("Frisbee Golf - Three Holes (Classic C)",      ItemType.progression),
    WSRItem("Frisbee Golf - Nine Holes (Resort)",          ItemType.progression),
    WSRItem("Frisbee Golf - Nine Holes (Classic)",         ItemType.progression),
    WSRItem("Frisbee Golf - Eighteen Holes",               ItemType.progression),

    # TODO: Finish the list . . .

# fmt: on
]
