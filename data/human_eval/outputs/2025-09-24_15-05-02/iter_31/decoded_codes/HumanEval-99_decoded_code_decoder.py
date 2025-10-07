from math import floor, ceil
from typing import Union


def closest_integer(string_value: str) -> int:
    if string_value.count('.') == 1:
        while string_value and string_value[-1] == '0':
            string_value = string_value[:-1]

    numerical_value = float(string_value) if string_value else 0.0

    if len(string_value) >= 2 and string_value[-2:] == '.5':
        if numerical_value > 0:
            result = ceil(numerical_value)
        else:
            result = floor(numerical_value)
    elif len(string_value) > 0:
        result = round(numerical_value)
    else:
        result = 0

    return result