from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    lowest_value: float = float('inf')
    highest_value: float = float('-inf')
    for element in list_of_numbers:
        if element < lowest_value:
            lowest_value = element
        if element > highest_value:
            highest_value = element

    range_value: float = highest_value - lowest_value
    normalized_values: List[float] = []
    iterator: int = 0
    while iterator < len(list_of_numbers):
        current_element: float = list_of_numbers[iterator]
        adjusted_value: float = (current_element - lowest_value) / range_value  # safe as range_value > 0 below
        normalized_values.append(adjusted_value)
        iterator += 1

    return normalized_values