from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    length: int = len(sequence_of_numbers)
    while position < length:
        current_element: int = sequence_of_numbers[position]
        if not (position % 2 != 0 or current_element % 2 != 1):
            accumulator += current_element
        position += 1
    return accumulator