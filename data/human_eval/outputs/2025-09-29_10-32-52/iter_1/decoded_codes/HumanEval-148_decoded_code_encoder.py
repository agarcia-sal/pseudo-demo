from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planet_names: Tuple[str, ...] = (
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune"
    )
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index: int = planet_names.index(planet1)
    planet2_index: int = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return planet_names[planet1_index + 1 : planet2_index]
    else:
        return planet_names[planet2_index + 1 : planet1_index]