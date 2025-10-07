from math import sqrt
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    sum_1 = param_x + param_y
    sum_2 = param_x + param_z
    sum_3 = param_y + param_z
    invalid_flag = (sum_1 <= param_z) or (sum_2 <= param_y) or (sum_3 <= param_x)

    if invalid_flag:
        return -1

    half_perimeter = (param_x + param_y + param_z) / 2

    temp_1 = half_perimeter - param_x
    temp_2 = half_perimeter - param_y
    temp_3 = half_perimeter - param_z

    raw_area = half_perimeter * temp_1 * temp_2 * temp_3
    raw_area = sqrt(raw_area)

    final_area = round(raw_area, 2)

    return final_area