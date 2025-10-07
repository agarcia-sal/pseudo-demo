from math import floor, ceil
from typing import Union

def closest_integer(value: str) -> int:
    # Strip trailing zeros after the decimal point if exactly one '.' is present
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]
    number = float(value) if value else 0.0

    if value.endswith('.5'):
        if number > 0:
            result = ceil(number)
        else:
            result = floor(number)
    elif value:
        result = round(number)
    else:
        result = 0

    return result