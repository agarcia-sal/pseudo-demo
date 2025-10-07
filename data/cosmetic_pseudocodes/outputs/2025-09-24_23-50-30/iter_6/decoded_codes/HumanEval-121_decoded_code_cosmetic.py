from typing import Sequence


def solution(sequence: Sequence[int]) -> int:
    total: int = 0
    pos: int = 0
    while pos < len(sequence):
        if (pos % 2 == 0) and (sequence[pos] % 2 == 1):
            total += sequence[pos]
        pos += 1
    return total