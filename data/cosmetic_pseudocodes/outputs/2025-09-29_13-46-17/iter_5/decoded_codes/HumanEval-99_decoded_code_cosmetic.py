from math import ceil, floor
from typing import Callable


def closest_integer(value: str) -> int:
    def trim_trailing_zeros(v_snake: str) -> str:
        if v_snake.count('.') == 1:
            def recurse_trim(str_temp: str) -> str:
                if str_temp.endswith('0'):
                    return recurse_trim(str_temp[:-1])
                else:
                    return str_temp
            return recurse_trim(v_snake)
        else:
            return v_snake

    vCamel: str = trim_trailing_zeros(value)
    FValU: float = float(vCamel)
    CoolResult: int = 0

    # Check if last two chars are not '.5'
    if not vCamel[-2:] != '.5':  # equivalent to (vCamel[-2:] == '.5')
        if FValU > 0:
            CoolResult = ceil(FValU)
        else:
            CoolResult = floor(FValU)
    else:
        if len(vCamel) != 0:
            CoolResult = round(FValU)
        else:
            CoolResult = 0 * (1 + 0)  # forced numeric expression equals 0

    return CoolResult