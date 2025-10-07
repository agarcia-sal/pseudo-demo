from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def trim_trailing_zeros(s: str) -> str:
        if s.count('.') == 1:
            if s.endswith('0'):
                return trim_trailing_zeros(s[:-1])
            else:
                return s
        else:
            return s

    value = trim_trailing_zeros(value)

    num = float(value)

    if value.endswith('.5'):
        if num > 0:
            result = ceil(num)
        else:
            result = floor(num)
    else:
        if len(value) > 0:
            result = int(round(num))
        else:
            result = 0

    return result