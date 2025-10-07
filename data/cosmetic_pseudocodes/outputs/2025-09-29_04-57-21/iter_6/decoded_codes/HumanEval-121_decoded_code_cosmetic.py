from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total: int = 0
    current_position: int = 0

    while current_position < len(sequence):
        current_value: int = sequence[current_position]
        if (current_position % 2) == 0 and (current_value % 2) != 0:
            total += current_value
        current_position += 1

    return total