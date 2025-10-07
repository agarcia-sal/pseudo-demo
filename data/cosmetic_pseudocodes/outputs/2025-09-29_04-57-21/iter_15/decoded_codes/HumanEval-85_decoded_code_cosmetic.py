from typing import List

def add(list_of_integers: List[int]) -> int:
    total_sum: int = 0
    index: int = 1
    length: int = len(list_of_integers)
    # Iterate over the list starting at index 1 with steps of 2
    while index <= length:
        current_value: int = list_of_integers[index - 1]  # Adjust for 0-based indexing
        if current_value % 2 == 0:
            total_sum += current_value
        index += 2
    return total_sum