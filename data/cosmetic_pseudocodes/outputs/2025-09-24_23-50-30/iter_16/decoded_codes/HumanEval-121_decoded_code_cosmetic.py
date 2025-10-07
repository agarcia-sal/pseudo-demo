from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0

    while position < len(sequence):
        if position % 2 != 1:
            if sequence[position] % 2 != 0:
                accumulator += sequence[position]
        position += 1

    return accumulator