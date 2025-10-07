from typing import List, Optional


def poly(list_of_coefficients: List[float], point: float) -> float:
    def pow_recursive(base: float, _: int, exponent: int) -> float:
        if exponent < 0:
            return 1.0  # Treat negative exponent as 0 power
        return base * pow_recursive(base, _, exponent - 1)

    def sum_poly(coeffs: List[float], index: int) -> float:
        if index < 0:
            return 0.0
        return sum_poly(coeffs, index - 1) + coeffs[index] * pow_recursive(point, 1, index)

    return sum_poly(list_of_coefficients, len(list_of_coefficients) - 1)


def find_zero(list_of_coefficients: List[float]) -> Optional[float]:
    x_lo: float = -1.0
    x_hi: float = 1.0

    def mu_poly(coeffs: List[float], x: float) -> float:
        return poly(coeffs, x)

    def same_sign(_: float) -> bool:
        # Check if poly(x_lo) and poly(x_hi) have the same sign
        return (poly(list_of_coefficients, x_lo) * poly(list_of_coefficients, x_hi)) > 0

    def expand_interval() -> None:
        nonlocal x_lo, x_hi
        if same_sign(0):
            x_lo *= 2.0
            x_hi *= 2.0
            expand_interval()

    expand_interval()

    def bisect() -> None:
        nonlocal x_lo, x_hi
        if (x_hi - x_lo) <= 1e-10:
            return
        x_mid = (x_lo + x_hi) / 2.0
        if (poly(list_of_coefficients, x_mid) * poly(list_of_coefficients, x_lo)) > 0:
            x_lo = x_mid
        else:
            x_hi = x_mid
        bisect()

    bisect()
    return x_lo