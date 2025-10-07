from math import floor
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> float:
    if not (param_x + param_y > param_z and param_x + param_z > param_y and param_y + param_z > param_x):
        return -1.0
    half_perimeter: float = (param_x + param_y + param_z) / 2
    intermediate_product: float = half_perimeter * (half_perimeter - param_x) * (half_perimeter - param_y) * (half_perimeter - param_z)
    raw_result: float = intermediate_product ** 0.5
    final_result: float = floor(raw_result * 100 + 0.5) / 100
    return final_result