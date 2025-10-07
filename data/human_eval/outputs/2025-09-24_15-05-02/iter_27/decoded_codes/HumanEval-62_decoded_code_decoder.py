from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    if not list_of_coefficients:
        raise ValueError("Input list_of_coefficients must not be empty")
    # The derivative coefficients: multiply each coefficient by its index, skipping the constant term at index 0
    return [index * coefficient for index, coefficient in enumerate(list_of_coefficients[1:], start=1)]