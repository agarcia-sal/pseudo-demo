from math import sqrt
from typing import Union


def triangle_area(a: float, b: float, c: float) -> Union[float, int]:
    # Check if the provided sides can form a triangle using the triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1

    s = (a + b + c) / 2  # semi-perimeter
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area