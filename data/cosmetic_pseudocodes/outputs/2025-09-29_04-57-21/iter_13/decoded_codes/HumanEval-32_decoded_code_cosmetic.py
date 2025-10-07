from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    accumulator: float = 0.0

    def helper(index: int, coeff: float) -> None:
        nonlocal accumulator
        accumulator += coeff * (point ** index)

    for index, coeff in enumerate(list_of_coefficients):
        helper(index, coeff)

    return accumulator


def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound: float = -1.0
    upper_bound: float = 1.0

    while True:
        val_low = poly(list_of_coefficients, lower_bound)
        val_high = poly(list_of_coefficients, upper_bound)

        # If signs differ or zero is hit, interval found
        if val_low * val_high <= 0:
            break
        lower_bound *= 2.0
        upper_bound *= 2.0

    def bisect(low: float, high: float) -> float:
        if (high - low) <= 1e-10:
            return low
        midpoint = (low + high) / 2.0
        val_mid = poly(list_of_coefficients, midpoint)
        val_low = poly(list_of_coefficients, low)
        if val_mid * val_low > 0:
            return bisect(midpoint, high)
        else:
            return bisect(low, midpoint)

    return bisect(lower_bound, upper_bound)