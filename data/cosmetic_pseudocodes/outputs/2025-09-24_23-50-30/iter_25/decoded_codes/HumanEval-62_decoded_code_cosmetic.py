from typing import List

def derivative(array_of_values: List[float]) -> List[float]:
    return [array_of_values[position] * (position - 1) for position in range(2, len(array_of_values))]