from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_value = max_number - min_number
    if range_value == 0:
        # All numbers are the same; return zeros as they all map to 0 in rescaling
        return [0.0 for _ in list_of_numbers]
    return [(number - min_number) / range_value for number in list_of_numbers]