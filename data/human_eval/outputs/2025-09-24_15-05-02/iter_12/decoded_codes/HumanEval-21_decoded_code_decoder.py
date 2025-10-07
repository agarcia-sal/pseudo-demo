from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_number = max_number - min_number
    if range_number == 0:
        # If all numbers are the same, return a list of zeros of the same length
        return [0.0 for _ in list_of_numbers]
    return [(x - min_number) / range_number for x in list_of_numbers]