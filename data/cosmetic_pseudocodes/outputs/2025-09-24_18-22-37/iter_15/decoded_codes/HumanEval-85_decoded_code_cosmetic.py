from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    iterator: int = 1
    while iterator <= len(sequence_of_numbers):
        current_element: int = sequence_of_numbers[iterator - 1]
        if current_element % 2 == 0:
            accumulator += current_element
        iterator += 2
    return accumulator