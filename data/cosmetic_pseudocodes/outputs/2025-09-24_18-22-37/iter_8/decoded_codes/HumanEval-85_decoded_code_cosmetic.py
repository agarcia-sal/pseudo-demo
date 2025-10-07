from typing import Sequence


def add(collection_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    current_index: int = 1
    max_index: int = len(collection_of_numbers)

    while current_index <= max_index:
        element_value: int = collection_of_numbers[current_index - 1]  # Adjust for 1-based index in pseudocode
        if element_value % 2 == 0:
            accumulator += element_value
        current_index += 2

    return accumulator