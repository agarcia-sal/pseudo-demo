from typing import List


def poly(coef_list: List[float], x_val: float) -> float:
    total = 0.0
    for idx, coef in enumerate(coef_list):
        total += coef * (x_val ** idx)
    return total


def find_zero(coef_list: List[float]) -> float:
    left_bound, right_bound = -1.0, 1.0
    # Expand interval until signs differ or zero found
    while poly(coef_list, left_bound) * poly(coef_list, right_bound) > 0:
        left_bound *= 2.0
        right_bound *= 2.0

    epsilon = 1e-10
    # Binary search to find root within precision epsilon
    while right_bound - left_bound > epsilon:
        midpoint = (left_bound + right_bound) / 2.0
        if poly(coef_list, midpoint) * poly(coef_list, left_bound) > 0:
            left_bound = midpoint
        else:
            right_bound = midpoint

    return left_bound