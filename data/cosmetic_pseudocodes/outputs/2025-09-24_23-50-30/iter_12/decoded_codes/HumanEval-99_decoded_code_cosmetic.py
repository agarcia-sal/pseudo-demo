from math import ceil, floor
from typing import Callable


def closest_integer(value: str) -> int:
    def strip_trailing_zeros(str_val: str) -> str:
        if '.' in str_val and str_val.count('.') == 1:
            def recur_trim(s: str) -> str:
                if s and s[-1] == '0':
                    return recur_trim(s[:-1])
                return s
            return recur_trim(str_val)
        return str_val

    trimmed_value: str = strip_trailing_zeros(value)
    try:
        float_num: float = float(trimmed_value)
    except ValueError:
        return 0

    if len(trimmed_value) > 1 and trimmed_value[-2:] == '.5':
        integer_result = ceil(float_num) if float_num > 0 else floor(float_num)
    elif len(trimmed_value) > 0:
        integer_result = round(float_num)
    else:
        integer_result = 0

    return integer_result