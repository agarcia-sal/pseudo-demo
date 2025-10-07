from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value[-1] == '0':
            value = value[:-1]

    num = float(value)

    if value[-2:] == '.5':
        if num > 0:
            result = ceil(num)
        else:
            result = floor(num)
    elif len(value) > 0:
        result = round(num)
    else:
        result = 0

    return result