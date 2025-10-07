from math import floor, ceil
from typing import Union

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value[-1] == '0' and len(value) > 1:
            value = value[:-1]

    try:
        num = float(value)
    except ValueError:
        return 0  # If value cannot be converted to float, return 0 as safe fallback

    if len(value) >= 2 and value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0

    return res