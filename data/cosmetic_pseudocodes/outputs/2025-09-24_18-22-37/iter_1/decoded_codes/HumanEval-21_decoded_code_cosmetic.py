from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_val: float = float('inf')
    max_val: float = float('-inf')
    for number in list_of_numbers:
        if number < min_val:
            min_val = number
        if number > max_val:
            max_val = number
    range_val = max_val - min_val
    if range_val == 0:
        # All numbers are equal; return zeros to avoid division by zero
        return [0.0 for _ in list_of_numbers]
    normalized_list = [(number - min_val) / range_val for number in list_of_numbers]
    return normalized_list