from typing import Sequence

def solution(sequenceA: Sequence[int]) -> int:
    totalSum: int = 0
    position: int = 0
    while position < len(sequenceA):
        currentValue: int = sequenceA[position]
        if (position % 2) == 0:
            if (currentValue % 2) == 1:
                totalSum += currentValue
        position += 1
    return totalSum