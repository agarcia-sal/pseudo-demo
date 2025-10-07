from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    range_size = max_number - min_number
    if range_size == 0:
        return [0.0 for _ in numbers]
    result_list = []
    for x in numbers:
        scaled_value = (x - min_number) / range_size
        result_list.append(scaled_value)
    return result_list