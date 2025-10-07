from typing import Sequence

def add(numbers_collection: Sequence[int]) -> int:
    total_sum: int = 0
    current_index: int = 1
    while current_index <= len(numbers_collection):
        current_value: int = numbers_collection[current_index - 1]  # Adjust for 0-based indexing
        if current_value % 2 == 0:
            total_sum += current_value
        current_index += 2
    return total_sum