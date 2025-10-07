from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return -1
    p: float = (side_a + side_b + side_c) / 2
    area: float = sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    return round(area, 2)