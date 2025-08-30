from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import ThePlanetCrafterWorld

def create_rules(world: "ThePlanetCrafterWorld"):
    world = world.multiworld
    player = world.player

    #set_rule(world.get_entrance("YellowCastlePort", player),
    #         lambda state: state.has("Yellow Key", player))