from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 == planet2 or planet1 not in planet_list or planet2 not in planet_list:
        return ()
    idx1 = planet_list.index(planet1)
    idx2 = planet_list.index(planet2)
    if idx1 > idx2:
        start, end_ = idx2 + 1, idx1
    else:
        start, end_ = idx1 + 1, idx2
    return tuple(planet_list[i] for i in range(start, end_))