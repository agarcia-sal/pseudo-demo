from math import floor, ceil
from typing import Union


def closest_integer(input_str: str) -> int:
    dot_count: int = input_str.count('.')

    if dot_count == 1:
        # strip trailing zeros after decimal point
        while input_str and input_str[-1] == '0':
            input_str = input_str[:-1]

    if not input_str:
        return 0

    decimal_value: float
    try:
        decimal_value = float(input_str)
    except ValueError:
        return 0

    length = len(input_str)

    if length >= 2 and input_str[-2:] == '.5':
        if decimal_value > 0:
            output_num = ceil(decimal_value)
        else:
            output_num = floor(decimal_value)
    elif length > 0:
        output_num = round(decimal_value)
    else:
        output_num = 0

    return output_num