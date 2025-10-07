from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total: int = 0
    position: int = 0

    while position < len(sequence):
        current: int = sequence[position]
        if (position & 1) == 0 and (current & 1) == 1:
            total += current
        position += 1

    return total