from typing import List

def derivative(array_of_coefficients: List[float]) -> List[float]:
    derived_terms: List[float] = []
    position: int = 1
    while position < len(array_of_coefficients):
        current_value: float = array_of_coefficients[position]
        derived_value: float = current_value * position
        derived_terms.append(derived_value)
        position += 1
    return derived_terms