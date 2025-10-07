from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total: int = 0
    position: int = 0

    while position < len(sequence):
        current_val: int = sequence[position]
        condition_one: bool = (position % 2 == 0)
        condition_two: bool = (current_val % 2 != 0)

        if condition_two:
            if condition_one:
                total += current_val

        position += 1

    return total