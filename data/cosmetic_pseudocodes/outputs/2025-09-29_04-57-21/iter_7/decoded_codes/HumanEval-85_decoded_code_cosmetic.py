from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    cumulative_sum: int = 0
    index: int = 1
    while index < len(sequence_of_numbers):
        current_value: int = sequence_of_numbers[index]
        if current_value % 2 == 0:
            cumulative_sum += current_value
        index += 2
    return cumulative_sum