from typing import Sequence

def add(array_of_numbers: Sequence[int]) -> int:
    total_accumulator: int = 0
    iterator_index: int = 1
    while iterator_index < len(array_of_numbers):
        if array_of_numbers[iterator_index] % 2 == 0:
            total_accumulator += array_of_numbers[iterator_index]
        iterator_index += 2
    return total_accumulator