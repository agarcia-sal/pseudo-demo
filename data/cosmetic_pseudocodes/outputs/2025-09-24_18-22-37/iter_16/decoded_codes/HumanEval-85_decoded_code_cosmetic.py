from typing import Sequence

def add(aSequence: Sequence[int]) -> int:
    accumulator: int = 0
    positionIndex: int = 1
    while positionIndex <= len(aSequence):
        currentElement: int = aSequence[positionIndex - 1]  # Adjust for 0-based indexing
        if currentElement % 2 == 0:
            accumulator += currentElement
        positionIndex += 2
    return accumulator