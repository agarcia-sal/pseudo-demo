from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def remove_trailing_zeros(s: str) -> str:
        while len(s) > 0 and s[-1] == '0':
            s = s[:-1]
        return s

    if value.count('.') == 1:
        value = remove_trailing_zeros(value)

    try:
        number = float(value)
    except ValueError:
        return 0

    if len(value) >= 2 and value[-2:] == '.5':
        return ceil(number) if number > 0 else floor(number)
    elif len(value) > 0:
        return round(number)
    else:
        return 0