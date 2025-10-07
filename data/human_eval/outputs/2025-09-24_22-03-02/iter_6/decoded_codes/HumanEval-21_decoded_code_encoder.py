from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    range_ = max_number - min_number
    if range_ == 0:
        return [0.0 for _ in numbers]
    return [(number - min_number) / range_ for number in numbers]