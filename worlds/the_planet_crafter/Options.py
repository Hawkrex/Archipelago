from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions

class Goal(Choice):
    """
    The goal to accomplish in order to complete the seed.
    - Prime Sentinel : Blow up the giant orb in the Ancient City (4 TTi / Large Explosion Device)
    - Prime Smugglers : Pay to leave (4 TTi / 250k Terra Tokens / 5 Solar Quartz)
    - Prime Wardens : Gather 10 Keys to leave
    """
    display_name = "Goal"

    option_prime_sentinel = 0
    option_prime_smugglers = 1
    option_prime_wardens = 2

    default = 0

@dataclass
class ThePlanetCrafterOptions(PerGameCommonOptions):
    goal: Goal
    death_link: DeathLink