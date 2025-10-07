from typing import List

def derivative(coefficients: List[float]) -> List[float]:
    return [i * c for i, c in enumerate(coefficients)][1:]