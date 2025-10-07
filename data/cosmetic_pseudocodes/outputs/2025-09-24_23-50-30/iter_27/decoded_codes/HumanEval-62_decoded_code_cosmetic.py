from typing import List

def derivative(array_of_values: List[float]) -> List[float]:
    result_array: List[float] = []
    position: int = 0
    while position < len(array_of_values):
        if position > 0:
            result_array.append(array_of_values[position] * position)
        position += 1
    return result_array