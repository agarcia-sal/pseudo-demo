from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    totalAccumulation: int = 0
    position: int = 0
    while position < len(sequence):
        element: int = sequence[position]
        isPositionEven: bool = (position % 2) == 0
        isElementOdd: bool = (element % 2) != 0
        if isPositionEven:
            if isElementOdd:
                totalAccumulation += element
        position += 1
    return totalAccumulation