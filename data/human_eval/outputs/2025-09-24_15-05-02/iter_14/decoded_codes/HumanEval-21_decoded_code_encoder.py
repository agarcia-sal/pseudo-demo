from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    result = []
    range_diff = max_number - min_number
    for x in numbers:
        if range_diff == 0:
            scaled_value = 0.0
        else:
            scaled_value = (x - min_number) / range_diff
        result.append(scaled_value)
    return result