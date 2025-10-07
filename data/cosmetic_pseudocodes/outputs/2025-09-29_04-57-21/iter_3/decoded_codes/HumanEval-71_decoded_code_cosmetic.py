from math import sqrt
from typing import Union

def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        return -1

    perimeter_half = (side_a + side_b + side_c) / 2
    part1 = perimeter_half
    part2 = perimeter_half - side_a
    part3 = perimeter_half - side_b
    part4 = perimeter_half - side_c

    raw_area = part1 * part2 * part3 * part4
    sqrt_area = sqrt(raw_area)

    final_area = round(sqrt_area, 2)

    return final_area