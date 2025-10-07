from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_width = max_number - min_number
    if range_width == 0:
        return [0.0] * len(list_of_numbers)  # All numbers are identical
    return [(num - min_number) / range_width for num in list_of_numbers]