from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    # Trim trailing zeros after decimal point if exactly one decimal point present
    if '.' in value and value.count('.') == 1:
        trim_index = len(value) - 1
        while trim_index >= 0 and value[trim_index] == '0':
            value = value[:trim_index]
            trim_index -= 1

    decimal_number: float = float(value) if value else 0.0

    if len(value) >= 2 and value[-2:] == '.5':
        if decimal_number > 0:
            closest_val = ceil(decimal_number)
        else:
            closest_val = floor(decimal_number)
    else:
        if len(value) == 0:
            closest_val = 0
        else:
            closest_val = round(decimal_number)

    return closest_val