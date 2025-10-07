from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    result = []
    range_number = max_number - min_number
    for x in numbers:
        scaled_value = (x - min_number) / range_number if range_number != 0 else 0.0
        result.append(scaled_value)
    return result