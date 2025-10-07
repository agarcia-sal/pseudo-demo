from typing import List

def derivative(coeffs: List[float]) -> List[float]:
    return [coeffs[i] * i for i in range(1, len(coeffs))]