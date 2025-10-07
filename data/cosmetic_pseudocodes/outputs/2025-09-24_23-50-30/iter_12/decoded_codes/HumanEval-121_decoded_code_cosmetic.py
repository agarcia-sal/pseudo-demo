from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total: int = 0
    position: int = 0

    while position < len(sequence):
        if (position % 2) == 0:
            if (sequence[position] % 2) != 0:
                total += sequence[position]
        position += 1

    return total