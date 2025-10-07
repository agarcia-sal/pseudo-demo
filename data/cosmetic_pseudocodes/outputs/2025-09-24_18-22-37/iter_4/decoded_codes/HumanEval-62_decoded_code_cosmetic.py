from typing import List

def derivative(coefficients: List[float]) -> List[float]:
    return [coefficients[idx] * idx for idx in range(1, len(coefficients))]