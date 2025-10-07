from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    cursor: int = 1
    while cursor <= len(sequence_of_numbers):
        current_element = sequence_of_numbers[cursor - 1]  # adjusting 1-based to 0-based indexing
        if current_element % 2 == 0:
            accumulator += current_element
        cursor += 2
    return accumulator