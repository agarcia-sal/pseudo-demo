from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        # Remove trailing zeros after decimal point
        while value[-1] == '0':
            value = value[:-1]

    temp = float(value) if value else 0.0

    if value[-2:] == '.5':
        answer = ceil(temp) if temp > 0 else floor(temp)
    elif len(value) > 0:
        answer = round(temp)
    else:
        answer = 0

    return answer