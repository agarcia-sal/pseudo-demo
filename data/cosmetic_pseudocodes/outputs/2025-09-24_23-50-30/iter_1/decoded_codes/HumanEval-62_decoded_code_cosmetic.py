from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [coeff * pos for pos, coeff in enumerate(list_of_coefficients) if pos > 0]