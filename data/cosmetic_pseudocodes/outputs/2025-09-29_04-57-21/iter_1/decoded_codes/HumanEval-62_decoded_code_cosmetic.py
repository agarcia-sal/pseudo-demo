from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [list_of_coefficients[pos] * pos for pos in range(1, len(list_of_coefficients))]