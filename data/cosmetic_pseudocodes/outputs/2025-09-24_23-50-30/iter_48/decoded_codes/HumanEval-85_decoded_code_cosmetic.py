from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    total_accumulator: int = 0
    index_counter: int = 1
    while index_counter <= len(sequence_of_numbers):
        if sequence_of_numbers[index_counter - 1] % 2 == 0:
            total_accumulator += sequence_of_numbers[index_counter - 1]
        index_counter += 2
    return total_accumulator