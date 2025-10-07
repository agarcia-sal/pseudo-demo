from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        return -1

    s: float = (side_a + side_b + side_c) / 2
    root_expression: float = s * (s - side_a) * (s - side_b) * (s - side_c)
    raw_area: float = sqrt(root_expression)
    final_area: float = round(raw_area, 2)

    return final_area