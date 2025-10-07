from typing import Tuple, Sequence

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planet_names: Tuple[str, ...] = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    condition_check: bool = (planet1 in planet_names) and (planet2 in planet_names) and (planet1 != planet2)
    if not condition_check:
        # If condition not met, return empty tuple (no execution specified)
        return ()

    idxA: int = planet_names.index(planet1)
    idxB: int = planet_names.index(planet2)

    if idxA <= idxB:
        return planet_names[idxA + 1 : idxB]
    else:
        return planet_names[idxB + 1 : idxA]