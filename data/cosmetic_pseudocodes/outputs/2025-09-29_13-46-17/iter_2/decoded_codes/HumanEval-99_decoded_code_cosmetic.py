from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def strip_trailing_zeros(str_val: str) -> str:
        if '.' in str_val and str_val.endswith('0'):
            return strip_trailing_zeros(str_val[:-1])
        return str_val

    if value.count('.') == 1:
        value = strip_trailing_zeros(value)

    num = float(value) if value else 0.0

    if len(value) > 0:
        if value[-2:] == '.5':
            result = ceil(num) if num > 0 else floor(num)
        else:
            result = round(num)
    else:
        result = 0

    return result