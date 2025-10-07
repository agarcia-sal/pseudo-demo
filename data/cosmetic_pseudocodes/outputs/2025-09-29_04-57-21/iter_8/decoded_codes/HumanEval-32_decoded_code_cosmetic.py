from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    total_sum: float = 0.0
    exponent_counter: int = 0
    while exponent_counter < len(list_of_coefficients):
        term = list_of_coefficients[exponent_counter] * (point ** exponent_counter)
        total_sum += term
        exponent_counter += 1
    return total_sum

def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound: float = -1.0
    upper_bound: float = 1.0

    # Expand bounds until they bracket a root
    while not (
        (poly(list_of_coefficients, lower_bound) < 0 and poly(list_of_coefficients, upper_bound) > 0) or
        (poly(list_of_coefficients, lower_bound) > 0 and poly(list_of_coefficients, upper_bound) < 0)
    ):
        lower_bound *= 2.0
        upper_bound *= 2.0

    while True:
        gap = upper_bound - lower_bound
        if gap <= 1e-10:
            break
        mid_point = lower_bound + gap / 2.0
        if poly(list_of_coefficients, mid_point) * poly(list_of_coefficients, lower_bound) > 0:
            lower_bound = mid_point
        else:
            upper_bound = mid_point

    return lower_bound