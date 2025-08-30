from typing import Dict
from BaseClasses import Location

from .datas.RegionDatas import REGION_DATAS_JSON

class ThePlanetCrafterLocation(Location):
    game = "The Planet Crafter"

location_table: Dict[str, int] = {}

def create_locations():
    next_location_id = 1

    for region_datas in REGION_DATAS_JSON:
        if "locations" in region_datas:
            for location in region_datas["locations"]:
                location_table[location] = next_location_id
                next_location_id += 1

    return location_table