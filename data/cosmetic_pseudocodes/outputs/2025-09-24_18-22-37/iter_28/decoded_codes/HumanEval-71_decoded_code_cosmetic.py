from math import sqrt
from typing import Union


def triangle_area(arg_x: float, arg_y: float, arg_z: float) -> Union[float, int]:
    invalid_flag: bool = False
    sum_one: float = arg_x + arg_y
    sum_two: float = arg_y + arg_z
    sum_three: float = arg_x + arg_z

    if sum_one <= arg_z:
        invalid_flag = True
    elif sum_three <= arg_y:
        invalid_flag = True
    elif sum_two <= arg_x:
        invalid_flag = True

    if invalid_flag:
        return -1

    half_perimeter: float = (arg_x + arg_y + arg_z) / 2
    diff_x: float = half_perimeter - arg_x
    diff_y: float = half_perimeter - arg_y
    diff_z: float = half_perimeter - arg_z

    product_val: float = half_perimeter * diff_x * diff_y * diff_z

    intermediate_area: float = sqrt(product_val)

    temp_area: float = intermediate_area * 100
    integral_part: int = int(temp_area // 1)
    remainder_part: float = temp_area - (integral_part * 1)

    if remainder_part >= 0.5:
        integral_part += 1

    final_area: float = integral_part / 100
    return final_area