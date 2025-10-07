from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def strip_trailing_zeros(str_val: str) -> str:
        if str_val.count('.') != 1:
            return str_val
        while str_val[-1] == '0':
            str_val = str_val[:-1]
            if str_val[-1] == '.':
                break  # avoid removing the decimal point itself
        return str_val

    processed_string: str = strip_trailing_zeros(value)
    if not processed_string:
        return 0
    try:
        number_value: float = float(processed_string)
    except ValueError:
        return 0

    if (
        len(processed_string) > 1
        and processed_string[-2:] == ".5"
    ):
        if number_value > 0:
            closest_num: int = ceil(number_value)
        else:
            closest_num = floor(number_value)
    elif len(processed_string) >= 1:
        closest_num = round(number_value)
    else:
        closest_num = 0

    return closest_num