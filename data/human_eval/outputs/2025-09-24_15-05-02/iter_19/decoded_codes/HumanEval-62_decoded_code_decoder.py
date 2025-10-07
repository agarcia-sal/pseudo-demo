from typing import List

def derivative(coefficients: List[int]) -> List[int]:
    return [index * coefficient for index, coefficient in enumerate(coefficients)][1:]