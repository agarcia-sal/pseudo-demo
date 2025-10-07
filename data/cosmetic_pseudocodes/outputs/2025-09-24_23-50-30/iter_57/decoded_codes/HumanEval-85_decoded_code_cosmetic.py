from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    cursor: int = 1
    while cursor < len(sequence):
        element: int = sequence[cursor]
        # Add element if it is even (element % 2 == 0)
        if not (element % 2 != 0):
            accumulator += element
        cursor += 2
    return accumulator