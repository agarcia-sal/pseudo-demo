from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    return sum(coef * (point ** idx) for idx, coef in enumerate(list_of_coefficients))


def find_zero(list_of_coefficients: List[float]) -> float:
    low, high = -1.0, 1.0
    while poly(list_of_coefficients, low) * poly(list_of_coefficients, high) > 0:
        low *= 2.0
        high *= 2.0
    while (high - low) > 1e-10:
        mid = (low + high) / 2.0
        if poly(list_of_coefficients, mid) * poly(list_of_coefficients, low) > 0:
            low = mid
        else:
            high = mid
    return low