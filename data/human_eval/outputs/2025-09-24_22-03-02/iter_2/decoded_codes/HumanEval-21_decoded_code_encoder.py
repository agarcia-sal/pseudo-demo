from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    result = []
    for x in numbers:
        scaled_value = (x - min_number) / (max_number - min_number)
        result.append(scaled_value)
    return result