from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    result = 0.0
    for index, coeff in enumerate(list_of_coefficients):
        result += coeff * (point ** index)
    return result

def find_zero(list_of_coefficients: List[float]) -> float:
    left_bound: float = -1.0
    right_bound: float = 1.0
    while poly(list_of_coefficients, left_bound) * poly(list_of_coefficients, right_bound) > 0:
        left_bound *= 2.0
        right_bound *= 2.0

    DELTA: float = 1e-10
    while (right_bound - left_bound) > DELTA:
        mid_point = (left_bound + right_bound) / 2.0
        product = poly(list_of_coefficients, mid_point) * poly(list_of_coefficients, left_bound)
        if product > 0:
            left_bound = mid_point
        else:
            right_bound = mid_point
    return left_bound