from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    decimal_point_count = 0
    for ch in value:
        if ch == '.':
            decimal_point_count += 1
    if decimal_point_count == 1:
        while value and value[-1] == '0':
            value = value[:-1]
    num = float(value) if value else 0.0
    length = len(value)
    if length >= 2:
        if value[-2:] == '.5':
            if num > 0:
                res = ceil(num)
            else:
                res = floor(num)
        elif length > 0:
            res = round(num)
        else:
            res = 0
    else:
        if length > 0:
            res = round(num)
        else:
            res = 0
    return int(res)