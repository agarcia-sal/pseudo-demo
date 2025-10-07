from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        # Trim trailing zeros after decimal point
        while value.endswith('0') and len(value) > 0:
            value = value[:-1]
    num_val = float(value) if value else 0.0
    if value[-2:] == '.5':
        if num_val > 0:
            answer = ceil(num_val)
        else:
            answer = floor(num_val)
    elif len(value) > 0:
        answer = round(num_val)
    else:
        answer = 0
    return answer