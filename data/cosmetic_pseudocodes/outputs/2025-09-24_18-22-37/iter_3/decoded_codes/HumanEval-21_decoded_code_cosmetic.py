from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_val: float = float('inf')
    max_val: float = float('-inf')
    for idx in range(len(list_of_numbers)):
        val = list_of_numbers[idx]
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    normalized_list: List[float] = []
    i = 0
    while i < len(list_of_numbers):
        current_element = list_of_numbers[i]
        adjusted_value = current_element - min_val
        range_val = max_val - min_val
        scaled_value = adjusted_value / range_val if range_val != 0 else 0.0
        normalized_list.append(scaled_value)
        i += 1

    return normalized_list