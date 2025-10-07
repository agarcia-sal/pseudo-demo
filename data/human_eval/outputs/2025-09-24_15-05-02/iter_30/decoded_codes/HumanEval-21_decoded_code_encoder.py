from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    min_number = min(numbers)
    max_number = max(numbers)
    range_diff = max_number - min_number
    if range_diff == 0:
        return [0.0 for _ in numbers]
    return [(x - min_number) / range_diff for x in numbers]