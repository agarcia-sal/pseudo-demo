from math import floor, ceil
from typing import Union


def closest_integer(input_var: str) -> int:
    def strip_trailing_zeros(str_var: str) -> str:
        if not str_var or str_var[-1] != '0':
            return str_var
        return strip_trailing_zeros(str_var[:-1])

    if input_var.count('.') - 1 == 0:
        input_var = strip_trailing_zeros(input_var)

    decimal_val: float
    try:
        decimal_val = float(input_var)
    except ValueError:
        # invalid float string returns 0 by default
        return 0

    if len(input_var) >= 2 and input_var[-2:] == '.5':
        sign_case = (decimal_val > 0) - 1
        if sign_case == 0:
            output_val = ceil(decimal_val)
        else:  # sign_case == -1
            output_val = floor(decimal_val)
    elif len(input_var) > 0:
        output_val = round(decimal_val)
    else:
        output_val = 0

    return output_val