from BaseClasses import Item, ItemClassification, Tutorial, Location, MultiWorld
from .items import item_table, create_item, create_itempool
from .regions import create_region
from .locations import location_table, is_location_valid, get_locations_names, get_total_locations
from .options import WSROptions, StampGoal, ChampionGoal, ProStatusGoal, Traps, StartingItems, SportsUnlockState, \
                    IncludeHardStamps, IncludeLongStamps, ExcludedStamps
from .types import CategoryIndex, SportIndex, WSRSport, ItemData
from worlds.AutoWorld import World, WebWorld, CollectionState
from worlds.generic.Rules import add_rule
from typing import List, Dict, TextIO
from worlds.LauncherComponents import Component, components, icon_paths, launch_subprocess, Type
from Utils import local_path

def run_client() -> None:
    """
    Launch the Wii Sports Resort Client
    """
    print("Running WSR Client")
    from .WSRClient import main

    launch_subprocess(main, name="WSRClient")

components.append(
    Component(
        "Wii Sports Resort Client",
        func=run_client,
        component_type=Type.CLIENT,
        file_identifier=(".apwsr"),
        icon="Wii Sports Resort"
    )
)
icon_paths["Wii Sports Resort"] = "ap:worlds.wsr/assets/icon.png"

class WSRWeb(WebWorld):
    """
    This class handles the web interface.

    The web interface includes the setup guide and the options page for generating YAMLs.
    """
    tutorials = [Tutorial(
        "Wii Sports Resort Setup Guide",
        "A guide to settup up Wii Sports Resort for archipelago on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kiwi", "Plyd", "Cyndifusic", "Dragonz"]
    )]
    theme = "ice"
    rich_text_options_doc = True

class WSRWorld(World):
    #VARS
    game = "Wii Sports Resort"
    item_name_to_id = {name: data.sport for name, data in item_table.items()}
    location_name_to_id = get_locations_names()
    options_dataclass = WSROptions
    options: WSROptions
    web = WSRWeb()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        #TODO
        pass

    def generate_early(self):
        #TODO: Starting Items
        return super().generate_early()

    def create_regions(self):
        #TODO: create regions
        pass

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def set_rules(self):
        #TODO: Set Rules
        pass

    def create_item(self, name: str) -> Item:
        return create_item(self, name)
    
    def collect(self, state: "CollectionState", item: "Item") -> bool:
        old_count: int = state.count(item.name, self.player)
        change = super().collect(state,item)
        if change and old_count == 0:
            if "Stamp" in item.name:
                state.prog_items[self.player]["Stamps"] += 1
            elif "Pro Status" in item.name:
                state.prog_items[self.player]["Pro Statuses"] += 1
            elif "Champion" in item.name:
                state.prog_items[self.player]["Champions"] += 1

        return change
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        old_count: int = state.count(item.name, self.player)
        change = super().collect(state,item)
        if change and old_count == 1:
            if "Stamp" in item.name:
                state.prog_items[self.player]["Stamps"] -= 1
            elif "Pro Status" in item.name:
                state.prog_items[self.player]["Pro Statuses"] -= 1
            elif "Champion" in item.name:
                state.prog_items[self.player]["Champions"] -= 1

        return change