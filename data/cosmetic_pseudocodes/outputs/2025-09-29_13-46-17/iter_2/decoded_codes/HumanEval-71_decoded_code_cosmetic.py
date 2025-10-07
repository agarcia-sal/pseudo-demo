from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    neg_one = -1
    if not (side_c < side_a + side_b) or not (side_b < side_a + side_c) or not (side_a < side_b + side_c):
        return neg_one
    else:
        s = (side_a + side_b + side_c) / 2
        area = sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        return round(area, 2)