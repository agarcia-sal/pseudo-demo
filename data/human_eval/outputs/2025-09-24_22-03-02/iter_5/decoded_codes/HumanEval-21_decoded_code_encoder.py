from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    denominator = max_number - min_number
    return [(x - min_number) / denominator for x in numbers]