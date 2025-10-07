from typing import Sequence

def add(array_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    index_var: int = 1
    while index_var <= len(array_of_numbers):
        current_value: int = array_of_numbers[index_var - 1]  # 1-based index to 0-based
        if current_value % 2 == 0:
            total_sum += current_value
        index_var += 2
    return total_sum