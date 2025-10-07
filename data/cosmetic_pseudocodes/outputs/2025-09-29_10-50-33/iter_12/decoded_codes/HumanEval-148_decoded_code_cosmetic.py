from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    bodies: Tuple[str, ...] = (
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune"
    )
    if planet1 in bodies and planet2 in bodies and planet1 != planet2:
        idxA = idxB = 0
        for place in range(len(bodies)):
            if bodies[place] == planet1:
                idxA = place
            if bodies[place] == planet2:
                idxB = place
        if not (idxA >= idxB):
            return bodies[idxA + 1 : idxB]
        else:
            return bodies[idxB + 1 : idxA]
    return ()