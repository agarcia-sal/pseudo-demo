from math import floor, ceil
from typing import Union

def closest_integer(param: str) -> int:
    if param.count('.') == 1:
        # Remove trailing zeros after decimal point
        while param.endswith('0') and len(param) > 0:
            param = param[:-1]
    number_val = float(param)
    if param[-2:] == '.5':
        if number_val > 0:
            res = ceil(number_val)
        else:
            res = floor(number_val)
    elif len(param) > 0:
        res = round(number_val)
    else:
        res = 0
    return res