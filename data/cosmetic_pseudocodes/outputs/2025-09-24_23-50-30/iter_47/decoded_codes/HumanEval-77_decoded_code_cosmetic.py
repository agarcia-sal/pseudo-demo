from typing import Union


def iscube(input_integer: int) -> bool:
    temp_abs: int = -input_integer if input_integer < 0 else input_integer
    temp_root: int = round(temp_abs ** (1/3))
    temp_cube: int = temp_root * temp_root * temp_root
    return temp_cube == temp_abs