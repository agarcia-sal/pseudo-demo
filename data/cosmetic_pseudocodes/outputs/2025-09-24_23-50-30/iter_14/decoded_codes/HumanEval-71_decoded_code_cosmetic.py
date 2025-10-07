from math import floor
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if not ((x1 + x2 > x3) and (x1 + x3 > x2) and (x2 + x3 > x1)):
        return -1
    semip: float = (x3 + x1 + x2) / 2
    val: float = semip * (semip - x3) * (semip - x2) * (semip - x1)
    root: float = val ** 0.5
    result: float = floor(root * 100 + 0.5) / 100
    return result