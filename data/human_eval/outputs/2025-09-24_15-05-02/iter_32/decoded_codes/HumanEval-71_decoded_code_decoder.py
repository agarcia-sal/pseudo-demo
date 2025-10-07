from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return -1
    semiperimeter = (side_a + side_b + side_c) / 2
    area_calc = semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c)
    area_value = sqrt(area_calc)
    rounded_area = round(area_value, 2)
    return rounded_area