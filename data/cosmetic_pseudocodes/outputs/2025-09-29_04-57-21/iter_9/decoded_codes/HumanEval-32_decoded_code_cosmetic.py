from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    total_value: float = 0.0
    exponent_index: int = 0
    for coefficient in list_of_coefficients:
        total_value += coefficient * (point ** exponent_index)
        exponent_index += 1
    return total_value

def find_zero(list_of_coefficients: List[float]) -> float:
    left_boundary: float = -1.0
    right_boundary: float = 1.0
    # Expand boundaries until the polynomial values at the boundaries have opposite signs
    while not (
        (poly(list_of_coefficients, left_boundary) < 0 and poly(list_of_coefficients, right_boundary) > 0) or
        (poly(list_of_coefficients, left_boundary) > 0 and poly(list_of_coefficients, right_boundary) < 0)
    ):
        left_boundary *= 2.0
        right_boundary *= 2.0

    precision_threshold: float = 1e-10
    while (right_boundary - left_boundary) > precision_threshold:
        midpoint: float = (left_boundary + right_boundary) / 2.0
        if poly(list_of_coefficients, midpoint) * poly(list_of_coefficients, left_boundary) > 0:
            left_boundary = midpoint
        else:
            right_boundary = midpoint
    return left_boundary