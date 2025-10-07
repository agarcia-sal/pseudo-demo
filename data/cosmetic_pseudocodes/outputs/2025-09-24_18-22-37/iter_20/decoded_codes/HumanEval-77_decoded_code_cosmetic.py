from typing import Union


def iscube(integer_value: int) -> bool:
    temp_abs: int = abs(integer_value)
    approx_root: int = round(temp_abs ** (1 / 3))
    cube_calc: int = approx_root * approx_root * approx_root
    return cube_calc == temp_abs