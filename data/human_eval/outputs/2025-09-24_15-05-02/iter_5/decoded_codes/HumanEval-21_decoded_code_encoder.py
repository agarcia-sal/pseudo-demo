from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    range_number = max_number - min_number
    if range_number == 0:
        return [0.0 for _ in numbers]
    return [(x - min_number) / range_number for x in numbers]