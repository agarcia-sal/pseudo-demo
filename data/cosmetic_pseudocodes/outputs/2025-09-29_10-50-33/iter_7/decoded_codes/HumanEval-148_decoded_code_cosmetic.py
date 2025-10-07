from typing import List, Tuple

def bf(celestialAlpha: str, celestialBeta: str) -> Tuple[str, ...]:
    orbitalSequence: List[str] = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if celestialAlpha == celestialBeta:
        return ()
    if celestialAlpha not in orbitalSequence or celestialBeta not in orbitalSequence:
        return ()
    alphaOrbitPos: int = orbitalSequence.index(celestialAlpha)
    betaOrbitPos: int = orbitalSequence.index(celestialBeta)
    if alphaOrbitPos < betaOrbitPos:
        # Return slice between alphaOrbitPos and betaOrbitPos, exclusive
        return tuple(orbitalSequence[alphaOrbitPos + 1 : betaOrbitPos])
    else:
        return tuple(orbitalSequence[betaOrbitPos + 1 : alphaOrbitPos])