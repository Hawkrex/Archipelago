from BaseClasses import Item, ItemClassification
from typing import NamedTuple, Dict

from .datas.Items import ITEMS_JSON

class ThePlanetCrafterItem(Item):
    game: str = "The Planet Crafter"

class ThePlanetCrafterItemData(NamedTuple):
    id: int
    classification: ItemClassification

item_table: Dict[str, ThePlanetCrafterItemData] = {}

def create_item_table():
    for item in ITEMS_JSON:
        item_table[item["Name"]] = ThePlanetCrafterItemData(item["Id"], convert_to_item_classification(item["Classification"]))

def convert_to_item_classification(json_classification: str) -> ItemClassification: 
    if json_classification == "progression":
        return ItemClassification.progression
    elif json_classification == "filler":
        return ItemClassification.filler
    return ItemClassification.useful

def build_item_name_to_id_table():
    return {name: data.id for name, data in item_table.items()}