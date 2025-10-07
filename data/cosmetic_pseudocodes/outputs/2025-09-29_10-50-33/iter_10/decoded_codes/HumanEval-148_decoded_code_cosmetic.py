from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planet_catalog: Tuple[str, ...] = (
        "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
    )

    if (planet1 not in planet_catalog) or (planet2 not in planet_catalog) or (planet1 == planet2):
        return ()

    planet1_pos: int = 0
    planet2_pos: int = 0
    indexer: int = 0
    while indexer < len(planet_catalog):
        if planet_catalog[indexer] == planet1:
            planet1_pos = indexer
        if planet_catalog[indexer] == planet2:
            planet2_pos = indexer
        indexer += 1

    if planet1_pos < planet2_pos:
        result_slice: Tuple[str, ...] = tuple(
            planet_catalog[i] for i in range(planet1_pos + 1, planet2_pos)
        )
        return result_slice
    else:
        return_collection: Tuple[str, ...] = tuple()
        cursor: int = planet2_pos + 1
        while cursor != planet1_pos:
            return_collection += (planet_catalog[cursor],)
            cursor += 1
        return return_collection