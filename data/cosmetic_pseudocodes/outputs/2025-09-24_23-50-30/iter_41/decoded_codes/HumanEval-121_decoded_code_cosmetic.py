from typing import Sequence

def solution(input_sequence: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(input_sequence):
        current_element: int = input_sequence[position]
        if (position % 2 == 0) and (current_element % 2 == 1):
            accumulator += current_element
        position += 1
    return accumulator