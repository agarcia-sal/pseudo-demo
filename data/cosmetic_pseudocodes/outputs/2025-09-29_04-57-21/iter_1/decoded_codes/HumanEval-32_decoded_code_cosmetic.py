from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    result: float = 0.0
    for index in range(len(list_of_coefficients)):
        result += list_of_coefficients[index] * (point ** index)
    return result

def find_zero(list_of_coefficients: List[float]) -> float:
    left_bound: float = -1.0
    right_bound: float = 1.0
    # Expand bounds until the polynomial values at bounds have opposite signs
    while poly(list_of_coefficients, left_bound) * poly(list_of_coefficients, right_bound) > 0:
        left_bound *= 2.0
        right_bound *= 2.0
    # Binary search for the zero within the interval
    while (right_bound - left_bound) > 1e-10:
        mid_point: float = (left_bound + right_bound) / 2.0
        if poly(list_of_coefficients, mid_point) * poly(list_of_coefficients, left_bound) > 0:
            left_bound = mid_point
        else:
            right_bound = mid_point
    return left_bound