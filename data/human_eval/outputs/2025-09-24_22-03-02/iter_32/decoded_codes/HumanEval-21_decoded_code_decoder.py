from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    min_number = min(numbers)
    max_number = max(numbers)
    if max_number == min_number:
        return [0.0 for _ in numbers]
    result = []
    for index in range(len(numbers)):
        x = numbers[index]
        numerator = x - min_number
        denominator = max_number - min_number
        scaled_value = numerator / denominator
        result.append(scaled_value)
    return result