from math import floor, ceil
from typing import Union


def closest_integer(input_str: str) -> int:
    dot_count: int = input_str.count('.')

    if dot_count == 1:
        # Remove trailing zeros from the fractional part
        while input_str and input_str[-1] == '0':
            input_str = input_str[:-1]

    temp_num: float = float(input_str) if input_str else 0.0

    last_two_chars: str = input_str[-2:] if len(input_str) >= 2 else ''

    if last_two_chars == '.5':
        if temp_num > 0:
            res: int = ceil(temp_num)
        else:
            res = floor(temp_num)
    else:
        res = round(temp_num) if input_str else 0

    return res