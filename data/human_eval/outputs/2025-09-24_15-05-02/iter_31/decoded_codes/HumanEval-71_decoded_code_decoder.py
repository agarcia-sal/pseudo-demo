from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if (
        side_a + side_b <= side_c
        or side_a + side_c <= side_b
        or side_b + side_c <= side_a
    ):
        return -1
    semi_perimeter = (side_a + side_b + side_c) / 2
    area_value = sqrt(
        semi_perimeter
        * (semi_perimeter - side_a)
        * (semi_perimeter - side_b)
        * (semi_perimeter - side_c)
    )
    return round(area_value, 2)