from math import floor, ceil
from typing import Union


def closest_integer(param: str) -> int:
    if sum(1 for char in param if char == '.') == 1:
        while param and param[-1] == '0':
            param = param[:-1]

    tmp = float(param) if param else 0.0

    if len(param) > 1 and param[-2:] == '.5':
        result = ceil(tmp) if tmp > 0 else floor(tmp)
    elif len(param) > 0:
        result = round(tmp)
    else:
        result = 0

    return result