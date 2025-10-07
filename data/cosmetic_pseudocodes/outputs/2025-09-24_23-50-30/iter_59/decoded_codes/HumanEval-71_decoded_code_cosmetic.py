from math import sqrt
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if not (x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1):
        return -1

    def helper_y(z1: float, z2: float, z3: float) -> float:
        return (z1 + z2 + z3) / 2

    a = helper_y(x1, x2, x3)
    b = a * (a - x1) * (a - x2) * (a - x3)

    def helper_c(v: float) -> float:
        return round(sqrt(v), 2)

    return helper_c(b)