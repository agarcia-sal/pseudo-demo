from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if not isinstance(value, str):
        raise ValueError("Input must be a string representing a number.")
    if not value:
        return 0

    # Remove trailing zeros after decimal point if exactly one '.'
    if value.count('.') == 1:
        # Remove trailing zeros at end
        while value.endswith('0'):
            value = value[:-1]
        # If the last char is '.', remove it as well (e.g. '12.' -> '12')
        if value.endswith('.'):
            value = value[:-1]

    try:
        num = float(value)
    except ValueError:
        raise ValueError(f"Invalid numeric string: {value}")

    # Check if the string (after trimming) ends with ".5"
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