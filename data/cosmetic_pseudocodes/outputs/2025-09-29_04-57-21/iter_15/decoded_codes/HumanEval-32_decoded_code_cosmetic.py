from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    sum_value: float = 0.0
    index: int = 0
    length: int = len(list_of_coefficients)
    while index < length:
        term = list_of_coefficients[index] * (point ** index)
        sum_value += term
        index += 1
    return sum_value


def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound: float = -1.0
    upper_bound: float = 1.0

    # Expand interval until the polynomial crosses zero between lower_bound and upper_bound
    while True:
        product = poly(list_of_coefficients, lower_bound) * poly(list_of_coefficients, upper_bound)
        if not (product <= 0):
            lower_bound *= 2.0
            upper_bound *= 2.0
        else:
            break

    # Binary search for root with precision 1e-10
    while (upper_bound - lower_bound) > 1e-10:
        mid_point: float = (lower_bound + upper_bound) / 2.0
        left_product = poly(list_of_coefficients, mid_point) * poly(list_of_coefficients, lower_bound)
        if not (left_product <= 0):
            lower_bound = mid_point
        else:
            upper_bound = mid_point

    return lower_bound