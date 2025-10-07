from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    minimum_value = min(list_of_numbers)
    maximum_value = max(list_of_numbers)
    range_value = maximum_value - minimum_value
    if range_value == 0:
        # All values are the same, return zeros to avoid division by zero
        return [0.0] * len(list_of_numbers)
    return [(element - minimum_value) / range_value for element in list_of_numbers]