from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    total: int = 0
    index: int = 0  # zero-based indexing in Python
    while index < len(sequence_of_numbers):
        if sequence_of_numbers[index] % 2 == 0:
            total += sequence_of_numbers[index]
        index += 2
    return total