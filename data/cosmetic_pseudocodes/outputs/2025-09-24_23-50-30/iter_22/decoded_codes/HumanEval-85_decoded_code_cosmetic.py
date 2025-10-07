from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    index: int = 1
    while index < len(sequence_of_numbers):
        if sequence_of_numbers[index] % 2 == 0:
            accumulator += sequence_of_numbers[index]
        index += 2
    return accumulator