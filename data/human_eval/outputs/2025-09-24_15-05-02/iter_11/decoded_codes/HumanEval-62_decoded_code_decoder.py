from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    derivative_coefficients = []
    for index, coefficient in enumerate(list_of_coefficients):
        derivative_coefficients.append(index * coefficient)
    return derivative_coefficients[1:]