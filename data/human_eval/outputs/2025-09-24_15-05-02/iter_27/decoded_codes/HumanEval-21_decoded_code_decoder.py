from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        raise ValueError("Input list cannot be empty")
    min_number: float = min(list_of_numbers)
    max_number: float = max(list_of_numbers)
    range_size: float = max_number - min_number
    if range_size == 0:
        # All elements are the same, return a list of zeros of the same length
        return [0.0 for _ in list_of_numbers]
    return [(element - min_number) / range_size for element in list_of_numbers]