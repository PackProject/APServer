from typing import Dict, TYPE_CHECKING

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

}

SWF_VS_LOCATIONS = {

}
SWF_PRC_LOCATIONS = {

}
SWF_SGL_LOCATIONS = {

}

WKB_LOCATIONS = {

}

FLD_LOCATIONS = {

}

DGL_LOCATIONS = {

}

ARC_LOCATIONS = {

}

BSK_3PT_LOCATIONS = {

}
BSK_VS_LOCATIONS = {

}

PNG_VS_LOCATIONS = {

}
PNG_RET_LOCATIONS = {

}

GLF_LOCATIONS = {

}

BWL_STD_LOCATIONS = {

}
BWL_100_LOCATIONS = {

}
BWL_WAL_LOCATIONS = {

}

JSK_LOCATIONS = {

}

CAN_LOCATIONS = {

}

BIC_LOCATIONS = {

}

PLN_LOCATIONS = {

}

OMK_LOCATIONS = {

}

HARD_STAMPS_LOCATIONS = {

}

LONG_STAMPS_LOCATIONS = {

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