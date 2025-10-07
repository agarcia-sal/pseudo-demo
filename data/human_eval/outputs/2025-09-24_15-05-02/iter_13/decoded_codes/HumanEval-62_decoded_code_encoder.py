from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [i * x for i, x in enumerate(list_of_coefficients)][1:]