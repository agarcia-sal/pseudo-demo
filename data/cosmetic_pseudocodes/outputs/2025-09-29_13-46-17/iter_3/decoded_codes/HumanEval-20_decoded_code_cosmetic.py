from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    def helper(
        i: int,
        j: int,
        currentClosest: Optional[Tuple[int, int]],
        currentDist: Optional[int],
    ) -> Optional[Tuple[int, int]]:
        if i == len(list_of_numbers):
            return currentClosest
        if j == len(list_of_numbers):
            return helper(i + 1, 0, currentClosest, currentDist)
        if i == j:
            return helper(i, j + 1, currentClosest, currentDist)

        valA = list_of_numbers[i]
        valB = list_of_numbers[j]
        absDiff = abs(valA - valB)

        if currentDist is None or absDiff < currentDist:
            newClosest = (valA, valB) if valA < valB else (valB, valA)
            return helper(i, j + 1, newClosest, absDiff)
        else:
            return helper(i, j + 1, currentClosest, currentDist)

    return helper(0, 0, None, None)