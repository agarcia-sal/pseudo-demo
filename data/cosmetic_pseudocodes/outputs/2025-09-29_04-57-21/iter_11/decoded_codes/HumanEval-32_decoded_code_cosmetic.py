from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    accumulator = 0.0
    for index, current_coefficient in enumerate(list_of_coefficients):
        accumulator += (point ** index) * current_coefficient
    return accumulator

def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound = -1.0
    upper_bound = 1.0

    while True:
        prod = poly(list_of_coefficients, lower_bound) * poly(list_of_coefficients, upper_bound)
        if prod <= 0:
            break
        lower_bound *= 2.0
        upper_bound *= 2.0

    while (upper_bound - lower_bound) > 1e-10:
        mid_point = (lower_bound + upper_bound) / 2.0
        prod_mid_lower = poly(list_of_coefficients, mid_point) * poly(list_of_coefficients, lower_bound)
        if prod_mid_lower > 0:
            lower_bound = mid_point
        else:
            upper_bound = mid_point

    return lower_bound