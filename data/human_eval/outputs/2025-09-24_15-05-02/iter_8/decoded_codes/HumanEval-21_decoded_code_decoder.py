from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    range_span = max_number - min_number
    if range_span == 0:
        return [0.0 for _ in numbers]
    return [(x - min_number) / range_span for x in numbers]