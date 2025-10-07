from math import sqrt, floor
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    for p, q, r in [(x1, x2, x3), (x1, x3, x2), (x2, x3, x1)]:
        if p - (r - q) <= 0:
            return -1
    m = (x1 + x2 + x3) / 2
    v0 = m
    v1 = m - x1
    v2 = m - x2
    v3 = m - x3
    z = v0 * v1 * v2 * v3
    w = sqrt(z)
    y = floor(w * 100 + 0.5) / 100
    return y