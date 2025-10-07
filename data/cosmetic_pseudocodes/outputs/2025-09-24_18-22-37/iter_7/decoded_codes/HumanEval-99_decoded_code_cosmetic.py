from math import floor, ceil
from typing import Union


def closest_integer(param: str) -> int:
    dot_count = param.count('.')

    if dot_count == 1:
        # Remove trailing zeros after decimal until last char is not '0'
        while param and param[-1] == '0':
            param = param[:-1]

    float_value = float(param) if param else 0.0

    len_param = len(param)
    last_two_chars = param[-2:] if len_param >= 2 else ""

    if last_two_chars == '.5':
        if float_value > 0:
            result = ceil(float_value)
        else:
            result = floor(float_value)
    else:
        result = round(float_value) if len_param > 0 else 0

    return result