from math import ceil, floor
from typing import Union


def closest_integer(input_val: str) -> int:
    def strip_trailing_zeros(str_val: str) -> str:
        if '.' in str_val:
            while str_val and str_val[-1] == '0':
                str_val = str_val[:-1]
        return str_val

    temp_val = strip_trailing_zeros(input_val)
    try:
        float_num = float(temp_val)
    except ValueError:
        return 0

    if len(temp_val) >= 2 and temp_val[-2:] == '.5':
        if float_num > 0:
            return ceil(float_num)
        else:
            return floor(float_num)
    elif len(temp_val) > 0:
        return round(float_num)
    else:
        return 0