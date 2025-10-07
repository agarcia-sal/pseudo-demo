from math import floor, ceil
from typing import Union


def closest_integer(input_value: str) -> int:
    def trim_trailing_zeros(str_val: str) -> str:
        if str_val.count('.') != 1:
            return str_val

        def remove_zeros_rec(s: str) -> str:
            if not s:
                return s
            if s[-1] == '0':
                return remove_zeros_rec(s[:-1])
            return s

        return remove_zeros_rec(str_val)

    cleaned_value = trim_trailing_zeros(input_value)

    try:
        numeric_value = float(cleaned_value)
    except ValueError:
        return 0

    if len(cleaned_value) > 0 and cleaned_value[-2:] == '.5':
        return ceil(numeric_value) if numeric_value > 0 else floor(numeric_value)
    if len(cleaned_value) > 0:
        return round(numeric_value)
    return 0