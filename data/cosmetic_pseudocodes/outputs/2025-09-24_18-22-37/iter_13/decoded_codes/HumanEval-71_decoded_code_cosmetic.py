from math import sqrt
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if not (x1 + x2 > x3):
        return -1
    if not (x1 + x3 > x2):
        return -1
    if not (x2 + x3 > x1):
        return -1
    p: float = (x1 + x2 + x3) / 2
    temp_val: float = p * (p - x1) * (p - x2) * (p - x3)
    result: float = round(sqrt(temp_val), 2)
    return result