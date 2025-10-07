from typing import List

def derivative(array_of_values: List[float]) -> List[float]:
    return [array_of_values[index] * index for index in range(1, len(array_of_values))]