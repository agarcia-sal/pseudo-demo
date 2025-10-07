from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    total: float = 0.0
    for index, coefficient in enumerate(list_of_coefficients):
        total += coefficient * (point ** index)
    return total

def find_zero(list_of_coefficients: List[float]) -> float:
    left_bound: float = -1.0
    right_bound: float = 1.0

    # Expand interval until a sign change is found
    while True:
        val_left = poly(list_of_coefficients, left_bound)
        val_right = poly(list_of_coefficients, right_bound)
        if val_left * val_right <= 0:
            break
        left_bound *= 2.0
        right_bound *= 2.0

    # Bisection method to refine root location
    while (right_bound - left_bound) > 1e-10:
        midpoint = left_bound + (right_bound - left_bound) / 2.0
        val_mid = poly(list_of_coefficients, midpoint)
        val_left = poly(list_of_coefficients, left_bound)
        if val_mid * val_left > 0:
            left_bound = midpoint
        else:
            right_bound = midpoint

    return left_bound