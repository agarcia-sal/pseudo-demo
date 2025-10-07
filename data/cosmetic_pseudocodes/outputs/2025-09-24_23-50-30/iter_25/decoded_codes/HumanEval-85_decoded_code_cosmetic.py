from typing import Sequence

def add(collection_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    index: int = 1
    while index < len(collection_of_numbers):
        current_value: int = collection_of_numbers[index]
        if current_value % 2 == 0:
            total_sum += current_value
        index += 2
    return total_sum