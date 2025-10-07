from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_span = max_number - min_number
    if range_span == 0:
        return [0.0] * len(list_of_numbers)
    return [(number - min_number) / range_span for number in list_of_numbers]