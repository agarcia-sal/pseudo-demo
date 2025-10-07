from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]

    x = float(value)

    if value.endswith('.5'):
        result = ceil(x) if x > 0 else floor(x)
    else:
        result = round(x) if len(value) > 0 else 0

    return result