from math import floor, ceil
from typing import Union


def closest_integer(val: str) -> int:
    def trim_trailing_zeros(str_input: str) -> str:
        if '.' not in str_input or str_input.count('.') != 1:
            return str_input
        if str_input[-1] == '0':
            return trim_trailing_zeros(str_input[:-1])
        return str_input

    clean_val: str = trim_trailing_zeros(val)
    if not clean_val:
        return 0

    try:
        number: float = float(clean_val)
    except ValueError:
        return 0

    if len(clean_val) >= 2 and clean_val[-2:] == '.5':
        return ceil(number) if number > 0 else floor(number)
    if len(clean_val) > 0:
        return round(number)
    return 0