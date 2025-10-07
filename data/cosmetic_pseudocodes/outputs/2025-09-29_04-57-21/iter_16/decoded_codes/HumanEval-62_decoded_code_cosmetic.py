from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    derivedCoefficients: List[float] = []
    position: int = 1

    while position < len(list_of_coefficients):
        derivedCoefficients.append(list_of_coefficients[position] * position)
        position += 1

    return derivedCoefficients