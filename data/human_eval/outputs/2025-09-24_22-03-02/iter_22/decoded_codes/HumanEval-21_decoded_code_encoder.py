from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
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
    while index < len(numbers):
        value = (numbers[index] - min_number) / (max_number - min_number)
        result.append(value)
        index += 1
    return result