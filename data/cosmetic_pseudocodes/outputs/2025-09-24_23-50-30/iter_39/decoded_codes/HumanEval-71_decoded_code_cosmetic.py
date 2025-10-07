from math import sqrt
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if (x1 + x2 > x3) and (x1 + x3 > x2) and (x2 + x3 > x1):
        y = (x1 + x2 + x3) / 2
        z = y * (y - x1) * (y - x2) * (y - x3)
        w = round(sqrt(z), 2)
        return w
    return -1