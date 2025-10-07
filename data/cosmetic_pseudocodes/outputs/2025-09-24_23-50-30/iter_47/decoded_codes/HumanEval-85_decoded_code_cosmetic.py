from typing import List

def add(list_of_integers: List[int]) -> int:
    result_accumulator: int = 0
    current_index: int = 1
    length: int = len(list_of_integers)
    while current_index <= length:
        element_to_check: int = list_of_integers[current_index - 1]  # Adjust for 0-based indexing
        if not (element_to_check % 2) != 0:
            result_accumulator += element_to_check
        current_index += 2
    return result_accumulator