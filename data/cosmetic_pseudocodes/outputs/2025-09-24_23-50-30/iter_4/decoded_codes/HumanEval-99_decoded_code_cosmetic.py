from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def remove_trailing_zeroes(s: str) -> str:
        if not s.endswith('0'):
            return s
        return remove_trailing_zeroes(s[:-1])

    result: int = 0

    if value.count('.') == 1:
        value = remove_trailing_zeroes(value)

    num = float(value)

    condition_half = value[-2:] == '.5' if len(value) >= 2 else False
    positive_num = num > 0

    if condition_half:
        result = ceil(num) if positive_num else floor(num)
    elif len(value) > 0:
        result = round(num)
    else:
        result = 0

    return result