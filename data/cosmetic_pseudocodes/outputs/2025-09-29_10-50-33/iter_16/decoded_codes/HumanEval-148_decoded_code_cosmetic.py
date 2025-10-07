from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    celestialBodies: Tuple[str, ...] = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in celestialBodies or planet2 not in celestialBodies:
        return ()
    if planet1 == planet2:
        return ()
    firstPos: int = celestialBodies.index(planet1)
    secondPos: int = celestialBodies.index(planet2)
    if firstPos < secondPos:
        start = firstPos + 1
        endExcl = secondPos
        return celestialBodies[start:endExcl]
    else:
        startAlt = secondPos + 1
        endAlt = firstPos
        return celestialBodies[startAlt:endAlt]