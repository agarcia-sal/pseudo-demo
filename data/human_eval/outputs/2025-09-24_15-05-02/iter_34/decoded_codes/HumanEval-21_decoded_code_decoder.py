from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    minimum_number: float = min(list_of_numbers)
    maximum_number: float = max(list_of_numbers)
    range_number: float = maximum_number - minimum_number
    if range_number == 0:
        # Avoid division by zero if all numbers are equal; return zeros accordingly
        return [0.0 for _ in list_of_numbers]
    return [(each_number - minimum_number) / range_number for each_number in list_of_numbers]