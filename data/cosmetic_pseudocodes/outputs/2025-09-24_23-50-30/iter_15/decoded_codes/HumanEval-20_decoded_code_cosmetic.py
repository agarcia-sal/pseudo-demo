from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    minDist: Optional[int] = None
    bestPair: Optional[Tuple[int, int]] = None
    idxA: int = 0

    while idxA < len(list_of_numbers):
        valA: int = list_of_numbers[idxA]
        idxB: int = 0

        while idxB < len(list_of_numbers):
            valB: int = list_of_numbers[idxB]

            if idxA == idxB:
                idxB += 1
                continue

            distCandidate: int = valA
            if valB < distCandidate:
                distCandidate = valB
            distCandidate = distCandidate - valA
            if distCandidate < 0:
                distCandidate = -distCandidate

            if minDist is None or distCandidate < minDist:
                minDist = distCandidate
                if valB < valA:
                    bestPair = (valB, valA)
                else:
                    bestPair = (valA, valB)

            idxB += 1
        idxA += 1

    return bestPair