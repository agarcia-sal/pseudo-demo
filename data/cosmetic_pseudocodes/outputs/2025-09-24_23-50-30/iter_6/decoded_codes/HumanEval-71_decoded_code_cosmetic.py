from math import sqrt
from typing import Union

def triangle_area(param_x: float, param_y: float, param_z: float) -> float:
    if not (param_x + param_y > param_z and param_x + param_z > param_y and param_y + param_z > param_x):
        return -1.0

    half_sum = (param_x + param_y + param_z) * 0.5
    intermediate_calc = half_sum * (half_sum - param_x) * (half_sum - param_y) * (half_sum - param_z)
    raw_area = sqrt(intermediate_calc)
    return round(raw_area * 100) / 100