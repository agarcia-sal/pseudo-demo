from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    index_counter: int = 1
    derivative_result: List[float] = []

    for coefficient in list_of_coefficients[1:]:
        derivative_result.append(coefficient * index_counter)
        index_counter += 1

    return derivative_result