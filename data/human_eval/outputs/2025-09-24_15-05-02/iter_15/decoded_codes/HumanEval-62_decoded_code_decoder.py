from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [i * c for i, c in enumerate(list_of_coefficients) if i > 0]