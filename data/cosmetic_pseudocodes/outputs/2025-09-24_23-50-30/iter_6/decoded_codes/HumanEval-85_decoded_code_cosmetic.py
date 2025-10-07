from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    indexCounter: int = 1
    while indexCounter <= len(sequence):
        candidate: int = sequence[indexCounter - 1]  # zero-based index adjustment
        if candidate % 2 == 0:
            accumulator += candidate
        indexCounter += 2
    return accumulator