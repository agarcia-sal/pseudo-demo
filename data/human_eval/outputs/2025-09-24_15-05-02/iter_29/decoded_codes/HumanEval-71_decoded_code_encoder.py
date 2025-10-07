from math import sqrt
from typing import Union


def triangle_area(a: float, b: float, c: float) -> float:
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    semi_perimeter = (a + b + c) / 2
    area = sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return round(area, 2)