from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    diff_threshold: float = 0.0
    lowest_value: float = float("inf")
    highest_value: float = float("-inf")
    idx_counter: int = 0

    while idx_counter < len(list_of_numbers):
        current_value = list_of_numbers[idx_counter]
        if current_value < lowest_value:
            lowest_value = current_value
        else:
            if current_value > highest_value:
                highest_value = current_value
        idx_counter += 1

    diff_threshold = highest_value - lowest_value

    normalized_list: List[float] = []
    position_tracker: int = 0

    while position_tracker < len(list_of_numbers):
        element = list_of_numbers[position_tracker]
        shifted_val = element - lowest_value
        scaled_val = shifted_val / diff_threshold if diff_threshold != 0 else 0.0
        normalized_list.append(scaled_val)
        position_tracker += 1

    return normalized_list