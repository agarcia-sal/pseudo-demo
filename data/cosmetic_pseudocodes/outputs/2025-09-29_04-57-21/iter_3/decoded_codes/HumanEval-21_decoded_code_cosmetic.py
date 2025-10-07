from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    lowest_value: float = float('inf')
    highest_value: float = float('-inf')

    for current_value in list_of_numbers:
        if current_value < lowest_value:
            lowest_value = current_value
        if current_value > highest_value:
            highest_value = current_value

    range_value = highest_value - lowest_value

    def normalize_value(value: float) -> float:
        # Handle zero range by returning 0.0 for all values
        return (value - lowest_value) / range_value if range_value != 0 else 0.0

    result_list: List[float] = [normalize_value(element) for element in list_of_numbers]

    return result_list