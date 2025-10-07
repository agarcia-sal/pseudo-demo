from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_number:
            min_number = numbers[i]
    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    result = []
    for i in range(len(numbers)):
        x = numbers[i]
        scaled_value = (x - min_number) / (max_number - min_number)
        result.append(scaled_value)
    return result