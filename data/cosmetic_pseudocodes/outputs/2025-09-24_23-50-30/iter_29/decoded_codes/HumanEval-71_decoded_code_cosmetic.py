from math import sqrt
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> float:
    # Check for triangle inequality; return -1 if not a valid triangle
    if not (x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1):
        return -1.0

    p = (x1 + x2 + x3) / 2
    q = p * (p - x1) * (p - x2) * (p - x3)
    r = round(sqrt(q), 2)

    return r