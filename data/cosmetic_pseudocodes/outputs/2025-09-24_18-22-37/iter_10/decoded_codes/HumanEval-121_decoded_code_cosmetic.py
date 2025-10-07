from typing import Sequence


def solution(sequence_of_numbers: Sequence[int]) -> int:
    accumulated_sum: int = 0
    position: int = 0
    while position < len(sequence_of_numbers):
        current_element: int = sequence_of_numbers[position]
        if position % 2 == 0:
            if current_element % 2 == 1:
                accumulated_sum += current_element
        position += 1
    return accumulated_sum