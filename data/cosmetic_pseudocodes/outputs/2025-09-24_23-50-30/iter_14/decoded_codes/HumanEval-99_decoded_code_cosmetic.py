from math import floor, ceil
from typing import Callable

def closest_integer(input_str: str) -> int:
    def trim_trailing_zeros(str_val: str) -> str:
        if str_val.count('.') != 1:
            return str_val
        while True:
            last_char_index = len(str_val) - 1
            if str_val[last_char_index] != '0':
                return str_val
            str_val = str_val[:last_char_index]

    trimmed_str = trim_trailing_zeros(input_str)
    if len(trimmed_str) == 0:
        return 0

    float_num = float(trimmed_str)

    if len(trimmed_str) >= 2 and trimmed_str[-2:] == '.5':
        if float_num <= 0:
            return floor(float_num)
        return ceil(float_num)

    return round(float_num)