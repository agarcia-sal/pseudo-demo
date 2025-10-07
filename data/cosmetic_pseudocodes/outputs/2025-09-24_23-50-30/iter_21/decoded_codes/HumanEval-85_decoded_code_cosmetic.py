from typing import Sequence

def add(numbers_collection: Sequence[int]) -> int:
    accumulator: int = 0
    idx: int = 1
    while idx <= len(numbers_collection):
        current_element: int = numbers_collection[idx - 1]  # Adjust for 0-based indexing
        if (current_element % 2) == 0:
            accumulator += current_element
        idx += 2
    return accumulator