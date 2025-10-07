from typing import List

def derivative(list_of_coefficients: List[int]) -> List[int]:
    return [index * coefficient for index, coefficient in enumerate(list_of_coefficients[1:], start=1)]