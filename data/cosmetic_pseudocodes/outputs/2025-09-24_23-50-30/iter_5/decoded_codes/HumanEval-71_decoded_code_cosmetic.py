from math import sqrt
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if (x1 + x2) <= x3 or (x1 + x3) <= x2 or (x2 + x3) <= x1:
        return -1

    p: float = (x1 + x2 + x3) * 0.5
    val: float = sqrt(p * (p - x1) * (p - x2) * (p - x3))
    return round(val * 100) / 100