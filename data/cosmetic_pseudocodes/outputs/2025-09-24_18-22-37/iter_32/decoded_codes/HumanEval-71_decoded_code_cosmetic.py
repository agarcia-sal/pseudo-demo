from math import sqrt
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    if not ((param_x + param_y) > param_z and (param_x + param_z) > param_y and (param_y + param_z) > param_x):
        return -1

    half_perimeter: float = (param_x + param_y + param_z) / 2

    temp1: float = half_perimeter
    temp2: float = half_perimeter - param_x
    temp3: float = half_perimeter - param_y
    temp4: float = half_perimeter - param_z

    raw_area: float = temp1 * temp2 * temp3 * temp4

    computed_area: float = sqrt(raw_area)

    final_result: float = round(computed_area * 100) / 100

    return final_result