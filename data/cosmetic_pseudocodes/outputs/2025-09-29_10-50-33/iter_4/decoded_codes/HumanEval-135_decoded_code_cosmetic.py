from typing import List

def can_arrange(array: List[int]) -> int:
    positionTracker: int = -1
    stepCounter: int = 1

    while stepCounter < len(array):
        if not (array[stepCounter - 1] <= array[stepCounter]):
            positionTracker = stepCounter
        stepCounter += 1

    return positionTracker