from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        # Trim trailing zeros after decimal point
        while value.endswith('0') and len(value) > 0:
            value = value[:-1]

    num = float(value) if value else 0.0

    if len(value) >= 2 and value[-2:] == '.5':
        res: int = ceil(num) if num > 0 else floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0

    return res