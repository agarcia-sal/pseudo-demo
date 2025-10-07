from typing import List

def derivative(coefficients: List[float]) -> List[float]:
    return [index * coefficient for index, coefficient in enumerate(coefficients) if index > 0]