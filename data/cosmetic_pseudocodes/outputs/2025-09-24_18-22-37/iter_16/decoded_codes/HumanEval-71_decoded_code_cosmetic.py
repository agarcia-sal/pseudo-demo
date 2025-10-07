from math import sqrt
from typing import Union


def triangle_area(x1: float, y2: float, z3: float) -> Union[float, int]:
    cond_a = (x1 + y2) <= z3
    cond_b = (x1 + z3) <= y2
    cond_c = (y2 + z3) <= x1
    if cond_a or cond_b or cond_c:
        return -1

    half_perim = (x1 + y2 + z3) / 2

    term_1 = half_perim
    term_2 = half_perim - x1
    term_3 = half_perim - y2
    term_4 = half_perim - z3

    product = term_1 * term_2 * term_3 * term_4

    area_raw = sqrt(product)

    area_final = round(area_raw * 100) / 100

    return area_final