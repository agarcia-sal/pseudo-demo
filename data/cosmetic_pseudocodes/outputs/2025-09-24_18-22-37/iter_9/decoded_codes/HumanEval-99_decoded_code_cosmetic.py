from math import floor, ceil
from typing import Union


def closest_integer(parameter_one: str) -> int:
    temp_digits = parameter_one.count('.')
    if temp_digits == 1:
        index_cursor = len(parameter_one)
        # Strip trailing zeros after decimal point
        while index_cursor > 0 and parameter_one[index_cursor - 1] == '0':
            parameter_one = parameter_one[: index_cursor - 1]
            index_cursor -= 1

    float_value = float(parameter_one)

    suffix_two_chars = parameter_one[-2:] if len(parameter_one) >= 2 else ''

    if suffix_two_chars == '.5':
        if float_value > 0:
            outcome = ceil(float_value)
        else:
            outcome = floor(float_value)
    else:
        if len(parameter_one) > 0:
            outcome = round(float_value)
        else:
            outcome = 0

    return outcome