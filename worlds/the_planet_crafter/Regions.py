from typing import Optional, TYPE_CHECKING

from BaseClasses import MultiWorld, Region
from .Locations import *
from .Items import *

from .datas.RegionDatas import REGION_DATAS_JSON
from .datas.RegionPaths import REGION_PATHS_JSON

if TYPE_CHECKING:
    from . import ThePlanetCrafterWorld

class ThePlanetCrafterRegion(Region):
    def __init__(self, name: str, player: int, multiworld: MultiWorld, hint: Optional[str] = None):
        super().__init__(name, player, multiworld, hint)

def create_regions(world: "ThePlanetCrafterWorld"):
    player = world.player
    multiworld = world.multiworld
    regions = multiworld.regions

    # Create regions and locations
    for region_datas in REGION_DATAS_JSON:
        region = ThePlanetCrafterRegion(region_datas["name"], player, multiworld)

        if "locations" in region_datas:
            for location in region_datas["locations"]:
                region.locations.append(ThePlanetCrafterLocation(player, location, location_table[location], region))
        
        regions.append(region)

    # Add menu and end region and its location
    regions.append(ThePlanetCrafterRegion("Menu", player, multiworld))

    region = ThePlanetCrafterRegion("End", player, multiworld)
    region.locations.append(ThePlanetCrafterLocation(player, "End", None, region))
    regions.append(region)

    # Create paths between regions
    for region_path in REGION_PATHS_JSON:
        from_region = regions.region_cache[player][region_path["fromRegion"]]
        to_region = regions.region_cache[player][region_path["toRegion"]]

        if "rule" in region_path:
            if region_path["rule"] == "Previous Region Emptied":
                location = ThePlanetCrafterLocation(player, f"{from_region.name} Emptied", None, from_region)
                from_region.locations.append(location)
                location.place_locked_item(world.create_event(f"{from_region.name} Emptied"))
                from_region.connect(to_region, f"{from_region.name} -> {to_region.name}", make_previous_region_emptied_rule(player, from_region.name))
            elif region_path["rule"] == "All progression items collected":
                from_region.connect(to_region, f"{from_region.name} -> {to_region.name}", make_all_prog_collected_rule(player))
        else:
            from_region.connect(to_region, f"{from_region.name} -> {to_region.name}")

        if region_path["twoWay"] == True:
            to_region.connect(from_region, f"{to_region.name} -> {from_region.name}")

def make_previous_region_emptied_rule(player: int, region_name: str):
    return lambda state: state.has(f"{region_name} Emptied", player)

def make_all_prog_collected_rule(player: int):
    return lambda state: all(state.has(prog_item_name, player) for prog_item_name, prog_item_data in item_table.items() if prog_item_data.classification == ItemClassification.progression)