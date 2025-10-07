from math import sqrt, floor
from typing import Union


def triangle_area(length_x: float, length_y: float, length_z: float) -> float:
    if not (length_x + length_y > length_z and length_x + length_z > length_y and length_y + length_z > length_x):
        return -1.0

    half_p: float = (length_z + length_x + length_y) * 0.5
    temp_area: float = sqrt(half_p * (half_p - length_z) * (half_p - length_y) * (half_p - length_x))
    final_result: float = floor(temp_area * 100 + 0.5) / 100
    return final_result