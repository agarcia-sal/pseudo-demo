from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = numbers[0]
    max_number = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] < min_number:
            min_number = numbers[index]
        if numbers[index] > max_number:
            max_number = numbers[index]
    result = []
    range_span = max_number - min_number
    for index in range(len(numbers)):
        x = numbers[index]
        if range_span == 0:
            scaled_value = 0.0
        else:
            scaled_value = (x - min_number) / range_span
        result.append(scaled_value)
    return result