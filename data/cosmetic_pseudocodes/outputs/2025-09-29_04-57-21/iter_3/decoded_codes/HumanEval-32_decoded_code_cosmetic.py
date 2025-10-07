from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    total_value = 0.0
    for index, coeff in enumerate(list_of_coefficients):
        total_value += coeff * (point ** index)
    return total_value


def find_zero(list_of_coefficients: List[float]) -> float:
    left_limit = -1.0
    right_limit = 1.0

    # Expand interval until f(left) * f(right) <= 0 for root bracketing
    while poly(list_of_coefficients, left_limit) * poly(list_of_coefficients, right_limit) > 0:
        left_limit *= 2.0
        right_limit *= 2.0

    def binary_search(low: float, high: float) -> float:
        if (high - low) <= 1e-10:
            return low
        mid_point = (low + high) / 2.0
        if poly(list_of_coefficients, mid_point) * poly(list_of_coefficients, low) > 0:
            return binary_search(mid_point, high)
        else:
            return binary_search(low, mid_point)

    return binary_search(left_limit, right_limit)