from typing import List

def derivative(coeffs: List[float]) -> List[float]:
    return [coeffs[position] * position for position in range(1, len(coeffs))]