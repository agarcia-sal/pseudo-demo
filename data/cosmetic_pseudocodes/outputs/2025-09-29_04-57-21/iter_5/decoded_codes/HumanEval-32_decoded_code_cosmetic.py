from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    total: float = 0.0
    exponent: int = 0
    for coefficient in list_of_coefficients:
        total += (point ** exponent) * coefficient
        exponent += 1
    return total


def find_zero(list_of_coefficients: List[float]) -> float:
    low: float = -1.0
    high: float = 1.0

    # Expand interval until poly(low) and poly(high) bracket a root
    while poly(list_of_coefficients, low) * poly(list_of_coefficients, high) > 0:
        low *= 2.0
        high *= 2.0

    # Bisection method to find root within tolerance
    while (high - low) > 1e-10:
        mid: float = (low + high) / 2.0
        if poly(list_of_coefficients, mid) * poly(list_of_coefficients, low) > 0:
            low = mid
        else:
            high = mid

    return low