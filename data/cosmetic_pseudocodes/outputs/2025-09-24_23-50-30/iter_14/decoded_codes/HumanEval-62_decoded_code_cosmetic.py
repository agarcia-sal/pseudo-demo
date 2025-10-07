from typing import List

def derivative(array_of_numbers: List[float]) -> List[float]:
    return [array_of_numbers[index] * index for index in range(1, len(array_of_numbers))]