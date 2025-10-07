from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    if max_number == min_number:
        return [0.0 for _ in numbers]
    result = []
    for x in numbers:
        transformed_value = (x - min_number) / (max_number - min_number)
        result.append(transformed_value)
    return result