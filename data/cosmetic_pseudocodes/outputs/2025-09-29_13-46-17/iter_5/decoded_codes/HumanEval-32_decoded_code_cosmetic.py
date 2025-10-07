from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    def inner_eval(idx: int, coeff: float) -> float:
        return coeff * (point ** idx)

    def helper(l: List[float], acc: float, i: int) -> float:
        if i == len(l):
            return acc
        return helper(l, acc + inner_eval(i, l[i]), i + 1)

    return helper(list_of_coefficients, 0.0, 0)


def find_zero(list_of_coefficients: List[float]) -> float:
    left_boundary: float = -1.0
    right_boundary: float = 1.0

    while True:
        val_left = poly(list_of_coefficients, left_boundary)
        val_right = poly(list_of_coefficients, right_boundary)
        if val_left * val_right <= 0:
            break
        left_boundary *= 2.0
        right_boundary *= 2.0

    def bisect(l: float, r: float) -> float:
        if (r - l) <= 1e-10:
            return l
        mid = (l + r) / 2.0
        if poly(list_of_coefficients, mid) * poly(list_of_coefficients, l) > 0:
            return bisect(mid, r)
        return bisect(l, mid)

    return bisect(left_boundary, right_boundary)