from typing import Tuple

def bf(orbA: str, orbB: str) -> Tuple[str, ...]:
    solar_bodies: Tuple[str, ...] = (
        "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
    )

    # Validate inputs: both must be in solar_bodies and distinct
    if orbA not in solar_bodies or orbB not in solar_bodies or orbA == orbB:
        return tuple()

    idxA: int = solar_bodies.index(orbA)
    idxB: int = solar_bodies.index(orbB)

    if idxA < idxB:
        # Return bodies between idxA and idxB, excluding orbA and orbB
        return solar_bodies[idxA + 1 : idxB]
    else:
        # Return bodies between idxB and idxA, excluding orbB and orbA
        return solar_bodies[idxB + 1 : idxA]