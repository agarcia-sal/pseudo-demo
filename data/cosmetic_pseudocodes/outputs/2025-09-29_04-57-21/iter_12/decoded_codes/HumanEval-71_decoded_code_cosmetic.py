from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if not ((side_c < side_a + side_b) and (side_b < side_a + side_c) and (side_a < side_b + side_c)):
        return -1

    half_perim = (side_a + side_b + side_c) / 2
    product_term = half_perim * (half_perim - side_a) * (half_perim - side_b) * (half_perim - side_c)
    raw_area = sqrt(product_term)
    final_area = round(raw_area, 2)

    return final_area