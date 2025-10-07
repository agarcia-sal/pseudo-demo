from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    no_triangle = (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a)
    if no_triangle:
        return -1.0
    p = (side_a + side_b + side_c) / 2
    area = p * (p - side_a) * (p - side_b) * (p - side_c)
    result = round(sqrt(area), 2)
    return result