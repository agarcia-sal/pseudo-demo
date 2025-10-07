from math import sqrt
from typing import Union


def triangle_area(a: float, b: float, c: float) -> Union[float, int]:
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    area = round(area, 2)
    return area