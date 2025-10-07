from math import floor, ceil
from typing import Union


def closest_integer(data: str) -> int:
    def trim_trailing_zeros(strng: str) -> str:
        if not strng or strng[-1] != '0':
            return strng
        return trim_trailing_zeros(strng[:-1])

    if [c for c in data if c == '.'] == ['.']:
        data = trim_trailing_zeros(data)

    number_value = float(data) if data else 0.0

    if len(data) >= 2 and data[-2:] == '.5':
        if number_value > 0:
            result = ceil(number_value)
        else:
            result = floor(number_value)
    elif len(data) > 0:
        result = round(number_value)
    else:
        result = 0

    return result