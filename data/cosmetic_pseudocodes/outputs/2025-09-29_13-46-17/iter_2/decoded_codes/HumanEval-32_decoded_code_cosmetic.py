from typing import List, Tuple


def poly(list_of_coefficients: List[float], point: float) -> float:
    def recursive_sum(index: int, acc: float) -> float:
        if index == len(list_of_coefficients):
            return acc
        return recursive_sum(index + 1, acc + list_of_coefficients[index] * (point ** index))
    return recursive_sum(0, 0.0)


def find_zero(list_of_coefficients: List[float]) -> float:
    left_endpoint: float = -1.0
    right_endpoint: float = 1.0

    def expand_interval(left: float, right: float) -> Tuple[float, float]:
        if poly(list_of_coefficients, left) * poly(list_of_coefficients, right) <= 0:
            return left, right
        return expand_interval(left * 2.0, right * 2.0)

    left_endpoint, right_endpoint = expand_interval(left_endpoint, right_endpoint)

    def bisect(left: float, right: float) -> float:
        if (right - left) <= 1e-10:
            return left
        mid_point = (left + right) / 2.0
        if poly(list_of_coefficients, mid_point) * poly(list_of_coefficients, left) > 0:
            return bisect(mid_point, right)
        else:
            return bisect(left, mid_point)

    return bisect(left_endpoint, right_endpoint)