from math import floor
from typing import Union


def iscube(integer_value: int) -> bool:
    magnitude: int = -integer_value if integer_value < 0 else integer_value
    potential_root: float = magnitude ** (1 / 3)
    rounded_root: int = floor(potential_root + 0.5)
    check_cube: int = rounded_root * rounded_root * rounded_root
    return check_cube == magnitude