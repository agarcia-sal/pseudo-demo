from typing import Tuple

def bf(orbitalBodyA: str, orbitalBodyB: str) -> Tuple[str, ...]:
    celestialRoster = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    if orbitalBodyA not in celestialRoster:
        return ()
    if orbitalBodyB not in celestialRoster:
        return ()
    if orbitalBodyA == orbitalBodyB:
        return ()

    indexA = 0
    indexB = 0
    iterator = 0

    while iterator < len(celestialRoster):
        if celestialRoster[iterator] == orbitalBodyA:
            indexA = iterator
        if celestialRoster[iterator] == orbitalBodyB:
            indexB = iterator
        iterator += 1

    if indexB < indexA:
        startRange = indexB + 1
        finishRange = indexA
    else:
        startRange = indexA + 1
        finishRange = indexB

    betweenPlanets: Tuple[str, ...] = ()
    position = startRange
    while position < finishRange:
        betweenPlanets += (celestialRoster[position],)
        position += 1

    return betweenPlanets