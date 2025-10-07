from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    accumulator = 0
    index = 1
    while index <= len(sequence):
        if sequence[index - 1] % 2 != 1:
            accumulator += sequence[index - 1]
        index += 2
    return accumulator