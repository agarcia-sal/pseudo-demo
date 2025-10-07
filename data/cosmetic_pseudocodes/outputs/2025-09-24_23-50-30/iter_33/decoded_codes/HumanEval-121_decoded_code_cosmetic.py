from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator < len(sequence):
        element: int = sequence[iterator]
        if (element % 2 != 0) and (iterator % 2 == 0):
            accumulator += element
        iterator += 1
    return accumulator