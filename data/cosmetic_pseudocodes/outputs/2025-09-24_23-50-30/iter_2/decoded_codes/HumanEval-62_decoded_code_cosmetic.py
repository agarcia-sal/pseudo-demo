from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    result: List[float] = []
    i: int = len(list_of_coefficients)
    while i > 1:
        i -= 1
        result.insert(0, list_of_coefficients[i] * i)
    return result