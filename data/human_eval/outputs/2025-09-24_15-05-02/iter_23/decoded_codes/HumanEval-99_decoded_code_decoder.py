from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        # Remove trailing zeros after decimal point
        while len(value) > 1 and value[-1] == '0':
            value = value[:-1]
    num: float
    try:
        num = float(value)
    except (ValueError, TypeError):
        # Handle invalid string input gracefully by returning 0
        return 0
    if len(value) >= 2 and value[-2:] == '.5':
        if num > 0:
            res: int = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0
    return int(res)