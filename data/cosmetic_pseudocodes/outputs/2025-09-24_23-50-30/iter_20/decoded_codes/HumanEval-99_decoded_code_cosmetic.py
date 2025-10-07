from math import floor, ceil
from typing import Callable


def closest_integer(input_str: str) -> int:
    def remove_trailing_zeros(str_val: str) -> str:
        if '.' not in str_val:
            return str_val

        def inner_loop(s: str) -> str:
            # Recursively remove trailing zeros after decimal point
            if len(s) > 0 and s[-1] == '0':
                return inner_loop(s[:-1])
            return s

        return inner_loop(str_val)

    trimmed_str: str = remove_trailing_zeros(input_str)
    decimal_num: float = float(trimmed_str) if trimmed_str else 0.0

    if len(trimmed_str) == 0:
        output_num = 0
    elif len(trimmed_str) >= 2 and trimmed_str[-2:] == '.5':
        if decimal_num > 0:
            output_num = ceil(decimal_num)
        else:
            output_num = floor(decimal_num)
    else:
        output_num = round(decimal_num)

    return output_num