from math import floor, ceil
from typing import Union

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]

    num: float = float(value) if value else 0.0

    if value[-2:] == '.5' if len(value) >= 2 else False:
        res: int = ceil(num) if num > 0 else floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0

    return res