from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    min_number: float = min(list_of_numbers)
    max_number: float = max(list_of_numbers)
    if min_number == max_number:
        # When all values are the same, return zeros to avoid division by zero
        return [0.0 for _ in list_of_numbers]
    result_list: List[float] = []
    range_span: float = max_number - min_number
    for number in list_of_numbers:
        result_list.append((number - min_number) / range_span)
    return result_list