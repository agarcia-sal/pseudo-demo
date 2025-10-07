from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    valid_nums: List[float] = []
    index: int = 0
    while index < len(list_of_numbers):
        current_val = list_of_numbers[index]
        if current_val > 0:
            valid_nums.append(current_val)
        index += 1
    return valid_nums