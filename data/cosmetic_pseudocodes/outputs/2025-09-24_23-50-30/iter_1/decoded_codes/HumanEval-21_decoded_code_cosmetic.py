from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    bottom_value = min(list_of_numbers)
    max_value = max(list_of_numbers)
    range_value = max_value - bottom_value
    if range_value == 0:
        # All values are identical; return zeros
        return [0.0] * len(list_of_numbers)
    return [(num - bottom_value) / range_value for num in list_of_numbers]