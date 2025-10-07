from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return -1
    semi = (side_a + side_b + side_c) / 2
    area_calc = (semi * (semi - side_a) * (semi - side_b) * (semi - side_c)) ** 0.5
    return round(area_calc, 2)