from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def helper(index: int, coeffs: List[float]) -> List[float]:
        if index >= len(coeffs):
            return []
        return [coeffs[index] * index] + helper(index + 1, coeffs)
    return helper(1, list_of_coefficients)