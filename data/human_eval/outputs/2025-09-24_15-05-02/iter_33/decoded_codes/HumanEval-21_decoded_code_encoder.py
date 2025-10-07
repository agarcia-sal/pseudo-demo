from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    minimum_number = min(list_of_numbers)
    maximum_number = max(list_of_numbers)
    range_ = maximum_number - minimum_number
    if range_ == 0:
        return [0.0 for _ in list_of_numbers]  # all numbers are the same, rescale to zeros
    return [(each_number - minimum_number) / range_ for each_number in list_of_numbers]