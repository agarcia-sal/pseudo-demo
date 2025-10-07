from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    minimum_number = min(list_of_numbers)
    maximum_number = max(list_of_numbers)
    range_ = maximum_number - minimum_number
    if range_ == 0:
        # All values are equal; return zeros as the scaled values
        return [0.0 for _ in list_of_numbers]
    return [(num - minimum_number) / range_ for num in list_of_numbers]