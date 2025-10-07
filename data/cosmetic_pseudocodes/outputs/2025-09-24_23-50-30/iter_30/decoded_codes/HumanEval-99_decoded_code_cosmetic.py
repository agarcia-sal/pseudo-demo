from math import floor, ceil
from typing import Union


def closest_integer(input_val: str) -> int:
    def trim_zero_trail(s: str) -> str:
        while s and s[-1] == '0':
            s = s[:-1]
        return s

    dot_count: int = input_val.count('.')

    if dot_count == 1:
        adjusted_val = trim_zero_trail(input_val)
    else:
        adjusted_val = input_val

    try:
        temp_num: float = float(adjusted_val)
    except ValueError:
        return 0  # fallback if conversion fails for some reason

    output_num: int

    if len(adjusted_val) >= 2 and adjusted_val[-2:] == '.5':
        if temp_num > 0:
            output_num = ceil(temp_num)
        else:
            output_num = floor(temp_num)
    elif len(adjusted_val) > 0:
        output_num = round(temp_num)
    else:
        output_num = 0

    return output_num