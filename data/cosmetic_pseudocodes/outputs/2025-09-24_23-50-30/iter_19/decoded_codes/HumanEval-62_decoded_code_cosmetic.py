from typing import List

def derivative(input_array: List[float]) -> List[float]:
    return [input_array[index] * index for index in range(1, len(input_array))]