from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        index = len(value) - 1
        # Remove trailing zeros after decimal point
        while index >= 0 and value[index] == '0' and '.' in value:
            value = value[:index]
            index -= 1

    number = float(value) if value else 0.0

    if value[-2:] == '.5' if len(value) >= 2 else False:
        if number > 0:
            output = ceil(number)
        else:
            output = floor(number)
    elif len(value) > 0:
        output = round(number)
    else:
        output = 0

    return output