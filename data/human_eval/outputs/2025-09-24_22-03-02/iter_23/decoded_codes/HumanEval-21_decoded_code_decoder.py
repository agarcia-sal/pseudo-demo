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
    denom = max_number - min_number
    for index in range(len(numbers)):
        x = numbers[index]
        rescaled_value = (x - min_number) / denom if denom != 0 else 0.0
        result.append(rescaled_value)
    return result