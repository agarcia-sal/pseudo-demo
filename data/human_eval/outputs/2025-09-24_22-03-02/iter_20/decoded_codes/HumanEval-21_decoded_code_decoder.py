from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    min_number = numbers[0]
    max_number = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] < min_number:
            min_number = numbers[index]
        if numbers[index] > max_number:
            max_number = numbers[index]
        index += 1
    result = []
    index = 0
    range_val = max_number - min_number
    while index < len(numbers):
        x = numbers[index]
        transformed_value = (x - min_number) / range_val if range_val != 0 else 0.0
        result.append(transformed_value)
        index += 1
    return result