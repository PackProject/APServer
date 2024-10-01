from worlds.AutoWorld import World
from .options import WSROptions
from .regions import WSRRegion
from .locations import WSRLocation
from .locations import *
from BaseClasses import Entrance


class WSRWorld(World):
    game = "Wii Sports Resort"

    options_dataclass = WSROptions
    options: WSROptions

    item_name_to_id = {}
    location_name_to_id = {}

    #
    # Create a list of all game regions
    #
    def create_regions(self):
        # Game begins from the menu region
        menu = WSRRegion("Menu", self.player, self.multiworld)
        self.multiworld.regions += menu

# fmt: off
        swf_vs = WSRRegion("Swordplay (Duel)", self.player, self.multiworld)
        swf_vs.add_locations(SWF_VS_LOCATIONS, WSRLocation)

        swf_prc = WSRRegion("Swordplay (Speed Slice)", self.player, self.multiworld)
        swf_prc.add_locations(SWF_PRC_LOCATIONS, WSRLocation)

        swf_sgl = WSRRegion("Swordplay (Showdown)", self.player, self.multiworld)
        swf_sgl.add_locations(SWF_SGL_LOCATIONS, WSRLocation)

        wkb = WSRRegion("Wakeboarding", self.player, self.multiworld)
        wkb.add_locations(WKB_LOCATIONS, WSRLocation)

        fld = WSRRegion("Frisbee (Frisbee Dog)", self.player, self.multiworld)
        fld.add_locations(FLD_LOCATIONS, WSRLocation)

        dgl = WSRRegion("Frisbee (Frisbee Golf)", self.player, self.multiworld)
        dgl.add_locations(DGL_LOCATIONS, WSRLocation)

        arc = WSRRegion("Archery", self.player, self.multiworld)
        arc.add_locations(ARC_LOCATIONS, WSRLocation)

        bsk_3pt = WSRRegion("Basketball (3-Point Contest)", self.player, self.multiworld)
        bsk_3pt.add_locations(BSK_3PT_LOCATIONS, WSRLocation)

        bsk_vs = WSRRegion("Basketball (Pickup Game)", self.player, self.multiworld)
        bsk_vs.add_locations(BSK_VS_LOCATIONS, WSRLocation)

        png_vs = WSRRegion("Table Tennis (Match)", self.player, self.multiworld)
        png_vs.add_locations(PNG_VS_LOCATIONS, WSRLocation)

        png_ret = WSRRegion("Table Tennis (Return Challenge)", self.player, self.multiworld)
        png_ret.add_locations(PNG_RET_LOCATIONS, WSRLocation)

        glf = WSRRegion("Golf", self.player, self.multiworld)
        glf.add_locations(GLF_LOCATIONS, WSRLocation)

        bwl_std = WSRRegion("Bowling (Standard Game)", self.player, self.multiworld)
        bwl_std.add_locations(BWL_STD_LOCATIONS, WSRLocation)

        bwl_100 = WSRRegion("Bowling (100-Pin Game)", self.player, self.multiworld)
        bwl_100.add_locations(BWL_100_LOCATIONS, WSRLocation)

        bwl_wal = WSRRegion("Bowling (Spin Control)", self.player, self.multiworld)
        bwl_wal.add_locations(BWL_WAL_LOCATIONS, WSRLocation)

        jsk = WSRRegion("Power Cruising (Slalom Course)", self.player, self.multiworld)
        jsk.add_locations(JSK_LOCATIONS, WSRLocation)

        can = WSRRegion("Canoeing (Speed Challenge)", self.player, self.multiworld)
        can.add_locations(CAN_LOCATIONS, WSRLocation)

        bic = WSRRegion("Cycling (Road Race)", self.player, self.multiworld)
        bic.add_locations(BIC_LOCATIONS, WSRLocation)

        pln = WSRRegion("Air Sports (Island Flyover)", self.player, self.multiworld)
        pln.add_locations(PLN_LOCATIONS, WSRLocation)

        omk = WSRRegion("Air Sports (Skydiving)", self.player, self.multiworld)
        omk.add_locations(OMK_LOCATIONS, WSRLocation)
# fmt: on

        seq_regions = [
            swf_vs,
            swf_prc,
            swf_sgl,
            wkb,
            fld,
            dgl,
            arc,
            bsk_3pt,
            bsk_vs,
            png_vs,
            png_ret,
            glf,
            bwl_std,
            bwl_100,
            bwl_wal,
            jsk,
            can,
            bic,
            pln,
            omk
        ]

        # All categories can exit to the main menu
        for it in seq_regions:
            it.add_exits(menu)

        # menu.entrances += seq_regions

        # The menu can exit to any of the categories
        # menu.exits += seq_regions
