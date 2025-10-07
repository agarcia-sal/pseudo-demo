from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [i * list_of_coefficients[i] for i in range(1, len(list_of_coefficients))]