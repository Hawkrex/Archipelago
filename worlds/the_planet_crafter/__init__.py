from typing import List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World

from .Options import *
from .Items import *
from .Locations import *
from .Regions import *

class ThePlanetCrafterWeb(WebWorld):
    theme = "dirt"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up The Planet Crafter Randomizer software on your computer.",
        "English",
        "the_planet_crafter_setup_en.md",
        "the_planet_crafter_setup/en",
        ["Hawkrex"]
    )]

class ThePlanetCrafterWorld(World):
    """
    The Planet Crafter is a base building game on different planets where you have to terraform them
    to survive their harsh environment and develop a new ecosystem on them.
    """
    game = "The Planet Crafter"
    options_dataclass = ThePlanetCrafterOptions
    options: ThePlanetCrafterOptions
    required_client_version = (0, 6, 2)
    web = ThePlanetCrafterWeb()

    create_item_table()

    item_name_to_id = build_item_name_to_id_table()
    location_name_to_id = create_locations()

    filler_item = "NoItem"

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

        def is_filler(item: tuple[str, ThePlanetCrafterItemData]):
            if item[1].classification == ItemClassification.filler:
                return True
            else:
                return False

        filler_filter = filter(is_filler, item_table.items())
        filler_list = []
        for filler in filler_filter:
            filler_list.append(filler[0])

        # Should be activated with an option, NoItem should be the default filler
        #self.filler_item = self.random.choice(filler_list)

    def fill_slot_data(self) -> dict:
        # Put options, locations' contents and some additional data inside slot data
        options = [
            "goal", "death_link"
        ]

        slot_data = self.options.as_dict(*options)

        return slot_data

    def create_regions(self):
        Regions.create_regions(self)

    def create_item(self, name: str) -> ThePlanetCrafterItem:
        data = item_table[name]
        item = ThePlanetCrafterItem(name, data.classification, data.id, self.player)
        return item
    
    def create_event(self, name: str) -> ThePlanetCrafterItem:
        return ThePlanetCrafterItem(name, ItemClassification.progression, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.filler_item
    
    def create_items(self):
        item_pool: List[ThePlanetCrafterItem] = []

        for name in item_table.keys():
            item_pool.append(self.create_item(name))

        # Add a pre-placed fake win condition item
        self.multiworld.get_location("End", self.player).place_locked_item(self.create_event("Escape"))

        # Fill the rest of the item pool with filler item
        remaining_items = len(self.multiworld.get_unfilled_locations(self.player)) - len(item_pool)
        item_pool += [self.create_item(self.get_filler_item_name()) for _ in range(remaining_items)]

        self.multiworld.itempool += item_pool

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Escape", self.player)