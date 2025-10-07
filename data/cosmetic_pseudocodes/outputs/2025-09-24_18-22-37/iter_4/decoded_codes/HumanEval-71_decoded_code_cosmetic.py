from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    a = side_a
    b = side_b
    c = side_c
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1
    p = (a + b + c) / 2
    value = p * (p - a) * (p - b) * (p - c)
    root_val = sqrt(value)
    final_area = round(root_val * 100) / 100
    return final_area