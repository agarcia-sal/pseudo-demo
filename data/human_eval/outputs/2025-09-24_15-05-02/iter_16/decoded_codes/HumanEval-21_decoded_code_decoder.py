from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_value = max_number - min_number
    if range_value == 0:
        # All numbers are the same, map all to 0.0
        return [0.0 for _ in list_of_numbers]
    result_list: List[float] = []
    for number in list_of_numbers:
        scaled_value = (number - min_number) / range_value
        result_list.append(scaled_value)
    return result_list