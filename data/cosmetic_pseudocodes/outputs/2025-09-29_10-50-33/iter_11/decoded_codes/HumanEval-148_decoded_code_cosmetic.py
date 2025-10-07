from typing import Tuple

def bf(orbitA: str, orbitB: str) -> Tuple[str, ...]:
    celestialBodies = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if orbitA not in celestialBodies or orbitB not in celestialBodies or orbitA == orbitB:
        return ()
    firstIndex = celestialBodies.index(orbitA)
    secondIndex = celestialBodies.index(orbitB)
    if firstIndex < secondIndex:
        return celestialBodies[firstIndex + 1 : secondIndex]
    return celestialBodies[secondIndex + 1 : firstIndex]