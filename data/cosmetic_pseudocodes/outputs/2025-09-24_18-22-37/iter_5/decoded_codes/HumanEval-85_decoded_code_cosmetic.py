from typing import Sequence

def add(numbers_collection: Sequence[int]) -> int:
    index_counter = 1
    accumulated_sum = 0
    while index_counter <= len(numbers_collection):
        current_element = numbers_collection[index_counter - 1]  # Adjust for 0-based indexing
        if current_element % 2 == 0:
            accumulated_sum += current_element
        index_counter += 2
    return accumulated_sum