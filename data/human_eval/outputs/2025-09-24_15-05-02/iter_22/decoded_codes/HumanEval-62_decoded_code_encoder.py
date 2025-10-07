from typing import List

def derivative(coefficients: List[float]) -> List[float]:
    derivative_coefficients: List[float] = []
    for index in range(len(coefficients)):
        derivative_term = index * coefficients[index]
        derivative_coefficients.append(derivative_term)
    if derivative_coefficients:
        derivative_coefficients.pop(0)
    return derivative_coefficients