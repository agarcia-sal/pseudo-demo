from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    low_val: float = list_of_numbers[0]
    high_val: float = list_of_numbers[0]

    idx: int = 1
    while idx < len(list_of_numbers):
        val = list_of_numbers[idx]
        if val < low_val:
            low_val = val
        elif val > high_val:
            high_val = val
        idx += 1

    denominator = high_val - low_val
    result_list: List[float] = []
    pos = 0
    while pos < len(list_of_numbers):
        current_val = list_of_numbers[pos]
        scaled_val = (current_val - low_val) / denominator if denominator != 0 else 0.0
        result_list.append(scaled_val)
        pos += 1

    return result_list