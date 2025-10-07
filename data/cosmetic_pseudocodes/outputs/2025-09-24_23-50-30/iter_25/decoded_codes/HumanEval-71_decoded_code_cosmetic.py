from math import sqrt
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    if not (param_x + param_y > param_z and param_x + param_z > param_y and param_y + param_z > param_x):
        return -1
    temp_sum = (param_x + param_y + param_z) / 2
    calc_area = sqrt(temp_sum * (temp_sum - param_x) * (temp_sum - param_y) * (temp_sum - param_z))
    return round(calc_area, 2)