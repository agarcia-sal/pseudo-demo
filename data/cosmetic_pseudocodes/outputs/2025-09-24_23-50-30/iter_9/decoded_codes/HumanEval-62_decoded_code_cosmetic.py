from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    return [index * list_of_coefficients[index] for index in range(1, len(list_of_coefficients))]