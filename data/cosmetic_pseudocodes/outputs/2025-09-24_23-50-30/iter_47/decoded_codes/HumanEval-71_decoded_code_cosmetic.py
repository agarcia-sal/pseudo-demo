from math import sqrt
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    if not (param_x + param_y > param_z and param_x + param_z > param_y and param_y + param_z > param_x):
        return -1
    aux_m = (param_x + param_y + param_z) / 2
    val_r = sqrt(aux_m * (aux_m - param_x) * (aux_m - param_y) * (aux_m - param_z))
    return round(val_r * 100) / 100