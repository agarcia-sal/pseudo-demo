from typing import List

def rescale_to_unit(array_values: List[float]) -> List[float]:
    lowest_val: float = float('inf')
    highest_val: float = float('-inf')
    for idx in range(len(array_values)):
        current_val: float = array_values[idx]
        if current_val < lowest_val:
            lowest_val = current_val
        if current_val > highest_val:
            highest_val = current_val
    range_val: float = highest_val - lowest_val
    scaled_list: List[float] = []
    for element in array_values:
        temp_diff: float = element - lowest_val
        scaled_element: float = temp_diff / range_val if range_val != 0 else 0.0
        scaled_list.append(scaled_element)
    return scaled_list