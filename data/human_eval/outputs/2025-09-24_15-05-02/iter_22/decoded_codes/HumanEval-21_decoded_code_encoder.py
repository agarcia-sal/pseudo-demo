from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    minimum_value = min(list_of_numbers)
    maximum_value = max(list_of_numbers)
    range_value = maximum_value - minimum_value
    if range_value == 0:
        # All numbers are the same; return list of zeros
        return [0.0 for _ in list_of_numbers]
    rescaled_list: List[float] = []
    for number in list_of_numbers:
        scaled_value = (number - minimum_value) / range_value
        rescaled_list.append(scaled_value)
    return rescaled_list