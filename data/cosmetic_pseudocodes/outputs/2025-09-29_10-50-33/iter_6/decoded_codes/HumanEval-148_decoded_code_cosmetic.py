from typing import Iterator, Tuple

def bf(celestialA: str, celestialB: str) -> Iterator[str]:
    orbits: Tuple[str, ...] = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if celestialA in orbits and celestialB in orbits and celestialA != celestialB:
        indexA = orbits.index(celestialA)
        indexB = orbits.index(celestialB)
        if indexA < indexB:
            yield from orbits[indexA + 1 : indexB]
        else:
            yield from orbits[indexB + 1 : indexA]
    else:
        return