from typing import List

def add(list_of_integers: List[int]) -> int:
    total_accumulator: int = 0
    position_index: int = 1  # 1-based index per pseudocode
    while position_index <= len(list_of_integers):
        current_value: int = list_of_integers[position_index - 1]  # adjust for zero-based indexing
        if current_value % 2 == 0:
            total_accumulator += current_value
        position_index += 2
    return total_accumulator