from math import log, exp, isclose
from typing import Union


def iscube(integer_value: int) -> bool:
    magnitude_temp = abs(integer_value)
    if magnitude_temp == 0:
        return True  # 0 is a perfect cube
    root_guess = round(exp(log(magnitude_temp) / 3))
    cube_candidate = root_guess ** 3
    return cube_candidate == magnitude_temp