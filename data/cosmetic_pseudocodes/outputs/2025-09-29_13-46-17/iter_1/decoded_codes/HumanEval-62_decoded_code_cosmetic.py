from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [list_of_coefficients[position] * position for position in range(1, len(list_of_coefficients))]