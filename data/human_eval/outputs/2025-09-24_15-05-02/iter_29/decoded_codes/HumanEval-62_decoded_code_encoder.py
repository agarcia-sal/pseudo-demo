from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [i * coefficient for i, coefficient in enumerate(list_of_coefficients)][1:]