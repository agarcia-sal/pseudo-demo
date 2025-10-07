from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(sequence):
        element: int = sequence[position]
        if not (position % 2 != 0 or element % 2 != 1):
            accumulator += element
        position += 1
    return accumulator