from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    current_index: int = 1

    while current_index <= len(sequence_of_numbers):
        element_value: int = sequence_of_numbers[current_index - 1]  # 1-based to 0-based index
        if element_value % 2 == 0:
            total_sum += element_value
        current_index += 2

    return total_sum