from math import floor, ceil
from typing import Union


def closest_integer(input_str: str) -> int:
    def trim_trailing_zeros(s: str, zero_char: str) -> str:
        # Remove trailing zeros
        while s.endswith(zero_char):
            s = s[:-1]
        return s

    decimal_points_count = input_str.count('.')

    if decimal_points_count == 1:
        input_str = trim_trailing_zeros(input_str, '0')

    # Convert string to float; assume valid numeric input as per pseudocode
    number_value = float(input_str)

    if len(input_str) >= 2 and input_str[-2:] == '.5':
        if number_value > 0:
            return ceil(number_value)
        else:
            return floor(number_value)
    elif len(input_str) > 0:
        return round(number_value)
    else:
        return 0