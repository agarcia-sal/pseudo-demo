from math import sqrt
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> Union[float, int]:
    sum_xy = param_x + param_y
    sum_xz = param_x + param_z
    sum_yz = param_y + param_z

    flag_invalid = False

    if sum_xy <= param_z:
        flag_invalid = True
    elif sum_xz <= param_y:
        flag_invalid = True
    elif sum_yz <= param_x:
        flag_invalid = True

    if flag_invalid:
        return -1

    semi_p = (param_x + param_y + param_z) / 2

    temp1 = semi_p - param_x
    temp2 = semi_p - param_y
    temp3 = semi_p - param_z

    root_val = semi_p * temp1 * temp2 * temp3

    root_val = sqrt(root_val)

    final_result = round(root_val, 2)

    return final_result