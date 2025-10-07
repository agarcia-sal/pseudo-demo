from math import sqrt
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    if not (param_x + param_y > param_z and param_x + param_z > param_y and param_y + param_z > param_x):
        return -1
    half_perimeter: float = (param_x + param_y + param_z) / 2
    temp_area: float = half_perimeter * (half_perimeter - param_x) * (half_perimeter - param_y) * (half_perimeter - param_z)
    result_area: float = round(sqrt(temp_area), 2)
    return result_area