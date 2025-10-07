from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total = 0
    position = 0
    while position < len(sequence):
        # Add element if both position and element are odd (odd*odd=1)
        if (position % 2) * (sequence[position] % 2) == 1:
            total += sequence[position]
        position += 1
    return total