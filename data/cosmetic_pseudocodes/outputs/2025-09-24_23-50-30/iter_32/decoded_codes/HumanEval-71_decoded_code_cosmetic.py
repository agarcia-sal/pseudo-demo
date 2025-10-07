from math import sqrt
from typing import Union


def triangle_area(var_x: float, var_y: float, var_z: float) -> Union[float, int]:
    var_p: float = (var_x + var_y + var_z) / 2
    if not ((var_x + var_y > var_z) and (var_x + var_z > var_y) and (var_y + var_z > var_x)):
        return -1
    else:
        return round(sqrt(var_p * (var_p - var_x) * (var_p - var_y) * (var_p - var_z)), 2)