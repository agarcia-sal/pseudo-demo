from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    dot_count = 0
    index = 0
    while index < len(value):
        if value[index] == '.':
            dot_count += 1
        index += 1

    if dot_count == 1:
        trimmed_value = value
        while len(trimmed_value) > 0 and trimmed_value[-1] == '0':
            trimmed_value = trimmed_value[:-1]
        value = trimmed_value

    if not value:
        return 0

    num = float(value)

    if len(value) >= 2:
        if value[-2] == '.' and value[-1] == '5':
            if num > 0:
                result = ceil(num)
            else:
                result = floor(num)
        else:
            result = round(num)
    else:
        result = round(num)

    return result