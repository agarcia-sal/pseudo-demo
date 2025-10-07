from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    total: int = 0
    current_index: int = 1  # 1-based index in pseudocode corresponds to 1-based here

    while current_index <= len(sequence_of_numbers):
        element: int = sequence_of_numbers[current_index - 1]  # adjust for 0-based indexing
        if (element % 2) != 1:
            total += element
        current_index += 2

    return total