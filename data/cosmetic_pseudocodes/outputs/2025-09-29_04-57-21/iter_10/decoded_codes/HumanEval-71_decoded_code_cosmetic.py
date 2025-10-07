from math import sqrt
from typing import Union


def triangle_area(length_x: float, length_y: float, length_z: float) -> Union[float, int]:
    if not (length_x + length_y > length_z and length_x + length_z > length_y and length_y + length_z > length_x):
        return -1
    half_perimeter = (length_x + length_y + length_z) / 2
    product_term = half_perimeter * (half_perimeter - length_x) * (half_perimeter - length_y) * (half_perimeter - length_z)
    raw_area = sqrt(product_term)
    precise_area = round(raw_area, 2)
    return precise_area