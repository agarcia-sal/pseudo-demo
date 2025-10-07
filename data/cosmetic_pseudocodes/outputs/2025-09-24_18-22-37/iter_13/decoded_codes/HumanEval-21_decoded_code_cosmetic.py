from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_val: float = float('inf')
    max_val: float = float('-inf')
    idx: int = 0
    n: int = len(list_of_numbers)

    while idx < n:
        val = list_of_numbers[idx]
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
        idx += 1

    scaled_list: List[float] = []
    position: int = 0

    # Handle the edge case where all numbers are equal to avoid ZeroDivisionError
    denominator = max_val - min_val
    while position != n:
        current_element = list_of_numbers[position]
        difference_num = current_element - min_val
        normalized_element = difference_num / denominator if denominator != 0 else 0.0
        scaled_list.append(normalized_element)
        position += 1

    return scaled_list