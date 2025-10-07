from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    result: float = 0.0
    index: int = 0
    while index < len(list_of_coefficients):
        term = list_of_coefficients[index] * (point ** index)
        result += term
        index += 1
    return result


def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound: float = -1.0
    upper_bound: float = 1.0

    # Expand bounds until a sign change is found
    while poly(list_of_coefficients, lower_bound) * poly(list_of_coefficients, upper_bound) > 0:
        lower_bound *= 2.0
        upper_bound *= 2.0

    # Binary search for root with specified precision
    while (upper_bound - lower_bound) > 1e-10:
        midpoint = (upper_bound + lower_bound) / 2.0
        if poly(list_of_coefficients, midpoint) * poly(list_of_coefficients, lower_bound) <= 0:
            upper_bound = midpoint
        else:
            lower_bound = midpoint

    return lower_bound