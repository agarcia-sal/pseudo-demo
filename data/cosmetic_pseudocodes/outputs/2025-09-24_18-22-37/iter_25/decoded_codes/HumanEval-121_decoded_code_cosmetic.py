from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total: int = 0
    position: int = 0

    while position < len(sequence):
        value: int = sequence[position]
        is_position_even: bool = (position % 2) == 0
        is_value_odd: bool = (value % 2) != 0

        if is_position_even and is_value_odd:
            total += value

        position += 1

    return total