from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]
    number = float(value) if value else 0.0

    if value.endswith('.5'):
        if number > 0:
            output = ceil(number)
        else:
            output = floor(number)
    elif len(value) > 0:
        output = round(number)
    else:
        output = 0

    return output