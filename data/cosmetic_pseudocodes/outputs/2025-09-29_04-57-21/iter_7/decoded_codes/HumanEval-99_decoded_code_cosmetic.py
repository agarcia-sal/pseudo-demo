from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    # Remove trailing zeros after decimal point if value has exactly one '.'
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]

    number = float(value)

    if value[-2:] == ".5":
        if number > 0:
            result = ceil(number)
        else:
            result = floor(number)
    elif len(value) > 0:
        result = round(number)
    else:
        result = 0

    return result