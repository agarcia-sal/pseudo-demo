from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def helper(index: int, coeffs: List[float], result: List[float]) -> List[float]:
        if index >= len(coeffs):
            return result
        updated_result = result + [coeffs[index] * index]
        return helper(index + 1, coeffs, updated_result)
    return helper(1, list_of_coefficients, [])