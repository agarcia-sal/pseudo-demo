from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_size = max_number - min_number
    if range_size == 0:
        # All numbers are identical; rescale to 0 for all
        return [0.0] * len(list_of_numbers)
    rescaled_list: List[float] = []
    for number in list_of_numbers:
        rescaled_value = (number - min_number) / range_size
        rescaled_list.append(rescaled_value)
    return rescaled_list