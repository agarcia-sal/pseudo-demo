from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    range_value = max_number - min_number
    result = []
    index = 0
    while index < len(numbers):
        x = numbers[index]
        difference = x - min_number
        scaled_value = difference / range_value
        result.append(scaled_value)
        index += 1
    return result