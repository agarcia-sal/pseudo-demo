from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    minimum_number = min(list_of_numbers)
    maximum_number = max(list_of_numbers)
    range_span = maximum_number - minimum_number
    if range_span == 0:
        return [0.0] * len(list_of_numbers)
    return [(x - minimum_number) / range_span for x in list_of_numbers]