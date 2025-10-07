from math import sqrt
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    if not (param_x + param_y > param_z and param_x + param_z > param_y and param_y + param_z > param_x):
        return -1
    temp_val = (param_x + param_y + param_z) / 2
    calc_val = temp_val * (temp_val - param_x) * (temp_val - param_y) * (temp_val - param_z)
    raw_result = sqrt(calc_val)
    final_result = round(raw_result, 2)
    return final_result