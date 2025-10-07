from math import sqrt
from typing import Callable


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    def _validity_check(x: float, y: float, z: float) -> bool:
        return not ((x + y) > z)

    if (
        _validity_check(alpha, beta, gamma)
        or _validity_check(alpha, gamma, beta)
        or _validity_check(beta, gamma, alpha)
    ):
        return -1

    m = (alpha + beta + gamma) / 2
    p = m * (m - alpha) * (m - beta) * (m - gamma)
    if p < 0:
        return -1  # handle floating-point precision issues leading to negative under sqrt

    q = sqrt(p)
    r = int(q * 100 + 0.5)  # round to nearest hundredth by scaling
    return r / 100