from math import sqrt
from typing import Union

def triangle_area(length_x: float, length_y: float, length_z: float) -> float:
    if not (length_x + length_y > length_z and length_x + length_z > length_y and length_y + length_z > length_x):
        return -1.0

    half_perimeter: float = (length_x + length_y + length_z) * 0.5

    temp_product: float = half_perimeter * (half_perimeter - length_x)
    temp_product *= (half_perimeter - length_y) * (half_perimeter - length_z)

    raw_area: float = sqrt(temp_product)

    precise_area: float = round(raw_area, 2)

    return precise_area