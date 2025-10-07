from math import exp, log, floor
from typing import Union


def iscube(integer_value: int) -> bool:
    abs_val: int = abs(integer_value)
    # Calculate cube root approximation, rounded to nearest integer
    cube_root: int = round(exp(log(abs_val) / 3)) if abs_val != 0 else 0
    power: int = cube_root
    for _ in range(3):
        power *= cube_root
    return power == abs_val