from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    min_number = min(numbers)
    max_number = max(numbers)
    range_span = max_number - min_number
    if range_span == 0:
        return [0.0 for _ in numbers]
    rescaled_numbers = []
    for x in numbers:
        transformed_value = (x - min_number) / range_span
        rescaled_numbers.append(transformed_value)
    return rescaled_numbers