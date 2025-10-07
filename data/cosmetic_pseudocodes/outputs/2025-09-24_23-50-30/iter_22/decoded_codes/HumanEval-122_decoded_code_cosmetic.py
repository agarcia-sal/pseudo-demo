from typing import List

def add_elements(list_of_numbers: List[int], count: int) -> int:
    total_sum: int = 0
    idx: int = 0
    while idx < count and idx < len(list_of_numbers):
        current_value: int = list_of_numbers[idx]
        if len(str(current_value)) <= 2:
            total_sum += current_value
        idx += 1
    return total_sum