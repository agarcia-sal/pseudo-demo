from math import sqrt
from typing import Union


def triangle_area(length_x: float, length_y: float, length_z: float) -> float:
    if not (
        (length_x + length_y > length_z)
        and (length_x + length_z > length_y)
        and (length_y + length_z > length_x)
    ):
        return -1.0

    sum_lengths = length_x + length_y + length_z
    half_perimeter = sum_lengths / 2

    diff_x = half_perimeter - length_x
    diff_y = half_perimeter - length_y
    diff_z = half_perimeter - length_z

    under_root = half_perimeter * diff_x * diff_y * diff_z
    raw_area = sqrt(under_root)

    decimal_factor = 10 * 10  # 100
    scaled_area = raw_area * decimal_factor
    rounded_scaled_area = round(scaled_area)
    rounded_area = rounded_scaled_area / decimal_factor

    return rounded_area