from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    derived_terms: List[float] = []
    position: int = 1
    while position < len(list_of_coefficients):
        derived_terms.append(list_of_coefficients[position] * position)
        position += 1
    return derived_terms