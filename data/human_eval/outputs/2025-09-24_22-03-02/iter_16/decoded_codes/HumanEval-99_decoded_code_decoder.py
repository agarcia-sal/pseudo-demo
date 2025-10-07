from math import ceil, floor
from typing import Union

def closest_integer(value: str) -> int:
    count_of_dot = value.count('.')
    if count_of_dot == 1:
        while value.endswith('0'):
            value = value[:-1]
    num = float(value) if value else 0.0
    if value.endswith('.5'):
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0
    return res