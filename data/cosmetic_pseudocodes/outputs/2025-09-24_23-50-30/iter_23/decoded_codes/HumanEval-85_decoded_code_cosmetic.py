from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    total_accumulator: int = 0
    current_index: int = 1  # 1-based indexing per pseudocode
    length = len(sequence_of_numbers)
    while current_index <= length:
        num = sequence_of_numbers[current_index - 1]  # adjust to zero-based indexing
        if num % 2 == 0:
            total_accumulator += num
        current_index += 2
    return total_accumulator