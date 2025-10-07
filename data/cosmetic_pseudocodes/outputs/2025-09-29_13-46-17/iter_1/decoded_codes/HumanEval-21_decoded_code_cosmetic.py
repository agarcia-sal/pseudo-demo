from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_val = min(list_of_numbers)
    max_val = max(list_of_numbers)
    range_val = max_val - min_val
    if range_val == 0:
        # All numbers are equal; map all to 0.0 to avoid division by zero
        return [0.0] * len(list_of_numbers)
    return [(number - min_val) / range_val for number in list_of_numbers]