from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    total = 0.0
    for exponent, coefficient in enumerate(list_of_coefficients):
        total += coefficient * (point ** exponent)
    return total


def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound = -1.0
    upper_bound = 1.0
    while poly(list_of_coefficients, lower_bound) * poly(list_of_coefficients, upper_bound) > 0:
        lower_bound *= 2.0
        upper_bound *= 2.0

    delta = 1e-10
    while (upper_bound - lower_bound) > delta:
        midpoint = (lower_bound + upper_bound) / 2.0
        if poly(list_of_coefficients, midpoint) * poly(list_of_coefficients, lower_bound) > 0:
            lower_bound = midpoint
        else:
            upper_bound = midpoint

    return lower_bound