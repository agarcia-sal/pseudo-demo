from typing import List, Optional

def bf(argAlpha: str, argBeta: str) -> Optional[List[str]]:
    celestialSet = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    if argAlpha not in celestialSet:
        return None
    if argBeta not in celestialSet:
        return None
    if argAlpha == argBeta:
        return None

    alphaPos = 0
    indexFinder = 0
    while indexFinder < len(celestialSet):
        if celestialSet[indexFinder] == argAlpha:
            alphaPos = indexFinder
            break
        indexFinder += 1

    betaPos = 0
    iterator = 0
    while iterator < len(celestialSet):
        if celestialSet[iterator] == argBeta:
            betaPos = iterator
            break
        iterator += 1

    if alphaPos < betaPos:
        return list(celestialSet[alphaPos + 1:betaPos])
    else:
        return list(celestialSet[betaPos + 1:alphaPos])