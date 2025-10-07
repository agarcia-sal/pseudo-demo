from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    result = []
    index = 0
    while index < len(numbers):
        x = numbers[index]
        numerator = x - min_number
        denominator = max_number - min_number
        scaled_value = numerator / denominator
        result.append(scaled_value)
        index += 1
    return result