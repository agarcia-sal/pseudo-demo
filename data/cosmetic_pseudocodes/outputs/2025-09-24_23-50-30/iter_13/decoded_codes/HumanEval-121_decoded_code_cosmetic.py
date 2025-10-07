from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total_sum: int = 0
    position: int = 0
    while position < len(sequence):
        current_element: int = sequence[position]
        if position % 2 == 0:
            if current_element % 2 == 1:
                total_sum += current_element
        position += 1
    return total_sum