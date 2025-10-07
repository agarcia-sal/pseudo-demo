from typing import List

def bf(planet1: str, planet2: str) -> List[str]:
    planet_collection: List[str] = [
        "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
    ]
    if planet1 not in planet_collection or planet2 not in planet_collection or planet1 == planet2:
        return []
    idx_alpha: int = planet_collection.index(planet1)
    idx_beta: int = planet_collection.index(planet2)
    if idx_alpha < idx_beta:
        return planet_collection[idx_alpha + 1 : idx_beta]
    if idx_beta < idx_alpha:
        return planet_collection[idx_beta + 1 : idx_alpha]
    return []