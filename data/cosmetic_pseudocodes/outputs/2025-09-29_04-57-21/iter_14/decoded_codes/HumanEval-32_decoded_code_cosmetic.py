from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    acc: float = 0.0
    idx: int = 0
    while idx < len(list_of_coefficients):
        term = list_of_coefficients[idx] * (point ** idx)
        acc += term
        idx += 1
    return acc


def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound: float = -1.0
    upper_bound: float = 1.0
    # Expand interval until poly(lower_bound) < 0 or poly(upper_bound) < 0
    while not (poly(list_of_coefficients, lower_bound) < 0 or poly(list_of_coefficients, upper_bound) < 0):
        lower_bound *= 2.0
        upper_bound *= 2.0

    while (upper_bound - lower_bound) > 1e-10:
        midpoint = (upper_bound + lower_bound) / 2.0
        # Check if poly(midpoint) * poly(lower_bound) <= 0
        if not (poly(list_of_coefficients, midpoint) * poly(list_of_coefficients, lower_bound) > 0):
            upper_bound = midpoint
        else:
            lower_bound = midpoint

    return lower_bound