from math import sqrt
from typing import Union


def triangle_area(arg_x: float, arg_y: float, arg_z: float) -> Union[float, int]:
    if not (arg_x + arg_y > arg_z):
        return -1
    if not (arg_x + arg_z > arg_y):
        return -1
    if not (arg_y + arg_z > arg_x):
        return -1

    temp_p: float = (arg_x + arg_y + arg_z) / 2
    val1: float = temp_p
    val2: float = temp_p - arg_x
    val3: float = temp_p - arg_y
    val4: float = temp_p - arg_z
    root_arg: float = val1 * val2 * val3 * val4

    calc_area: float = sqrt(root_arg)
    rounded_value: float = round(calc_area, 2)

    return rounded_value