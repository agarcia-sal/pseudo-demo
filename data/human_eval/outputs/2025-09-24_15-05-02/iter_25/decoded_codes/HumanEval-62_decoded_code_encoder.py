from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    result: List[float] = []
    for i, x in enumerate(list_of_coefficients):
        term = i * x
        result.append(term)
    derivative_list = result[1:]
    return derivative_list