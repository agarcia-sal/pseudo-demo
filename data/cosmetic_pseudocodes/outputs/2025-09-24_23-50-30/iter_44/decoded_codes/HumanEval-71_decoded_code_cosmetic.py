from math import sqrt
from typing import Union

def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    if not ((param_x + param_y > param_z) and (param_x + param_z > param_y) and (param_y + param_z > param_x)):
        return -1
    temp_s: float = (param_x + param_y + param_z) / 2
    calc_area: float = sqrt(temp_s * (temp_s - param_x) * (temp_s - param_y) * (temp_s - param_z))
    result_val: float = round(calc_area * 100) / 100
    return result_val