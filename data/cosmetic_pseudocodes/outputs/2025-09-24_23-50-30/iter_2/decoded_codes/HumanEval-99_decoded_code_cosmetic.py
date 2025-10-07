from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    dot_count = value.count('.')
    if dot_count == 1:
        idx = len(value) - 1
        while True:
            if value[idx] != '0':
                break
            idx -= 1
            if idx < 0:
                break
        value = value[: idx + 1]

    num = 0.0
    if len(value) > 0:
        num = float(value)

    if not (len(value) >= 2 and value[-2:] == '.5'):
        if len(value) > 0:
            result = round(num)
        else:
            result = 0
    else:
        if num <= 0:
            result = floor(num)
        else:
            result = ceil(num)

    return int(result)