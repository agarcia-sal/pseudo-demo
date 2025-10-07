from typing import List


def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    lowest_value: float = min(list_of_numbers)
    highest_value: float = max(list_of_numbers)
    range_value: float = highest_value - lowest_value

    def normalize_element(index: int) -> List[float]:
        if index == len(list_of_numbers):
            return []
        current_element = list_of_numbers[index]
        # Handle the case where all elements are equal to avoid division by zero
        if range_value == 0:
            adjusted_value = 0.0
        else:
            adjusted_value = (current_element - lowest_value) / range_value
        return [adjusted_value] + normalize_element(index + 1)

    return normalize_element(0)