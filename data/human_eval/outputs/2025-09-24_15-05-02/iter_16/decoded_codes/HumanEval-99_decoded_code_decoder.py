from math import ceil, floor
from typing import Union

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        # Remove trailing zeros after decimal point
        while value[-1] == '0':
            value = value[:-1]
            if len(value) == 0:
                break

    num: float
    try:
        num = float(value)
    except ValueError:
        # If value cannot be converted to float, treat as zero
        return 0

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