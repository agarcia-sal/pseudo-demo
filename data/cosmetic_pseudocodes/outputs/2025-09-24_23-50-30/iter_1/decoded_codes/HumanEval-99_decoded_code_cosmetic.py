from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]

    if not value:
        return 0

    num = float(value)

    if value.endswith('.5'):
        result = ceil(num) if num > 0 else floor(num)
    else:
        result = round(num)

    return result