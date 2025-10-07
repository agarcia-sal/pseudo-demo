from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    index: int = 1
    while index <= len(sequence):
        if sequence[index - 1] % 2 == 0:
            accumulator += sequence[index - 1]
        index += 2
    return accumulator