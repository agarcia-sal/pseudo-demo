from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_ = max_number - min_number
    if range_ == 0:
        # Avoid division by zero; all elements are the same, so return zeros
        return [0.0 for _ in list_of_numbers]
    return [(element - min_number) / range_ for element in list_of_numbers]