from math import floor, ceil
from typing import Union


def closest_integer(omega: str) -> int:
    chars = omega
    dot_count = 0
    idx = 0

    while idx < len(chars):
        if chars[idx] == '.':
            dot_count += 1
        idx += 1

    if dot_count == 1:
        while chars and chars[-1] == '0':
            chars = chars[:-1]

    decimal_value = float(chars)

    suffix = ''
    if len(chars) >= 2:
        suffix = chars[-2:]

    if suffix == '.5':
        if decimal_value > 0:
            return ceil(decimal_value)
        else:
            return floor(decimal_value)

    if len(chars) > 0:
        return round(decimal_value)

    return 0