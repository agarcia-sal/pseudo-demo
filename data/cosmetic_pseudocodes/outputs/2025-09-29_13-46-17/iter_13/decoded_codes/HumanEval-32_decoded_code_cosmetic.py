from typing import List, Tuple


def poly(list_of_coefficients: List[float], point: float) -> float:
    def powerRecursive(base: float, exp: int, acc: int) -> float:
        if exp == acc:
            return 1.0
        return base * powerRecursive(base, exp, acc + 1)

    def summator(xw0: float, xw1: int, xw2: int) -> float:
        if xw1 == len(list_of_coefficients):
            return xw0
        return summator(xw0 + list_of_coefficients[xw1] * powerRecursive(point, xw1, 0), xw1 + 1, xw2)

    return summator(0.0, 0, 0)


def find_zero(list_of_coefficients: List[float]) -> float:
    def expand_bounds(scipr0: float, scipr1: float) -> Tuple[float, float]:
        val0 = poly(list_of_coefficients, scipr0)
        val1 = poly(list_of_coefficients, scipr1)
        if val0 * val1 <= 0:
            return (scipr0, scipr1)
        return expand_bounds(scipr0 * 2, scipr1 * 2)

    def bisect(low: float, high: float) -> float:
        if abs(high - low) <= 1e-10:
            return low
        mid = (low + high) / 2
        val_mid = poly(list_of_coefficients, mid)
        val_low = poly(list_of_coefficients, low)
        if val_mid * val_low > 0:
            return bisect(mid, high)
        return bisect(low, mid)

    alpha, beta = expand_bounds(-1.0, 1.0)
    return bisect(alpha, beta)