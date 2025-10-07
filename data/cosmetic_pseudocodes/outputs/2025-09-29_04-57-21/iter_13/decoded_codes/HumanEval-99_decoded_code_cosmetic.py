from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if '.' in value and value.count('.') == 1:
        while True:
            tail_char = value[-1]
            if tail_char != '0':
                break
            value = value[:-1]
    decimal_num = float(value) if value else 0.0

    if len(value) >= 2 and value[-2:] == '.5':
        if decimal_num > 0:
            return ceil(decimal_num)
        else:
            return floor(decimal_num)
    elif len(value) > 0:
        return round(decimal_num)
    else:
        return 0