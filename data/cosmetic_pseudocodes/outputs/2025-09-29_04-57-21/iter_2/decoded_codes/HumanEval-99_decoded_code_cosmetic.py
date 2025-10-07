from math import floor, ceil
from typing import Union


def closest_integer(input_str: str) -> int:
    if input_str.count('.') == 1:
        # Strip trailing zeros after decimal point
        while input_str[-1] == '0':
            input_str = input_str[:-1]
            if not input_str or input_str[-1] == '.':
                break

    try:
        numeric_val = float(input_str)
    except ValueError:
        return 0

    if input_str.endswith('.5'):
        return ceil(numeric_val) if numeric_val > 0 else floor(numeric_val)
    elif len(input_str) > 0:
        return round(numeric_val)
    else:
        return 0