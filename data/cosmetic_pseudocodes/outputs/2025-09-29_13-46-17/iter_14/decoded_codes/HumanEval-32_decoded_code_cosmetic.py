from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    accumulator: float = 0.0
    index: int = 0
    coefficients: List[float] = list_of_coefficients

    def helper(acc: float, val: float, idx: int) -> float:
        if idx >= len(coefficients):
            return val
        coeff: float = coefficients[idx]
        power_val: float = 1.0
        for _ in range(idx):
            power_val *= point
        return helper(acc, val + coeff * power_val, idx + 1)

    return helper(accumulator, 0.0, index)


def find_zero(list_of_coefficients: List[float]) -> float:
    left: float = -1.0
    right: float = 1.0

    def test_sign(l: float, r: float) -> bool:
        val_l = poly(list_of_coefficients, l)
        val_r = poly(list_of_coefficients, r)
        return (val_l * val_r) > 0.0

    while test_sign(left, right):
        left *= 2.0
        right *= 2.0

    def recurse(low: float, high: float) -> float:
        if (high - low) <= 1e-10:
            return low
        mid: float = (low + high) / 2.0
        product: float = poly(list_of_coefficients, mid) * poly(list_of_coefficients, low)
        if product > 0.0:
            return recurse(mid, high)
        else:
            return recurse(low, mid)

    return recurse(left, right)