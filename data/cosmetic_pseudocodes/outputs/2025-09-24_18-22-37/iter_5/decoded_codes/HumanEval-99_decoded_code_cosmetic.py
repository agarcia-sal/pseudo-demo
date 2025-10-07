from math import floor, ceil
from typing import Union


def closest_integer(input_str: str) -> int:
    dot_count = 0
    idx = 0
    while idx < len(input_str):
        if input_str[idx] == '.':
            dot_count += 1
        idx += 1

    if dot_count == 1:
        str_len = len(input_str)
        # Trim trailing zeros at the end of input_str
        while str_len > 0 and input_str[str_len - 1] == '0':
            input_str = input_str[: str_len - 1]
            str_len -= 1

    numeric_value = float(input_str) if input_str else 0.0

    if len(input_str) >= 2:
        # Check if input_str ends with ".5"
        if input_str[-2:] == '.5':
            if numeric_value > 0:
                return ceil(numeric_value)
            else:
                return floor(numeric_value)

    if len(input_str) > 0:
        return round(numeric_value)
    else:
        return 0