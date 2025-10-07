from math import floor, ceil
from typing import Union


def closest_integer(value_1: str) -> int:
    def trim_trailing_zeros(value_2: str) -> str:
        if value_2.count('.') == 1:
            while value_2[-1] == '0':
                value_2 = value_2[:-1]
        return value_2

    value_3 = trim_trailing_zeros(value_1)
    try:
        num_1 = float(value_3)
    except ValueError:
        return 0

    if len(value_3) >= 2 and value_3[-2:] == '.5':
        return ceil(num_1) if num_1 > 0 else floor(num_1)
    elif len(value_3) > 0:
        return round(num_1)
    else:
        return 0