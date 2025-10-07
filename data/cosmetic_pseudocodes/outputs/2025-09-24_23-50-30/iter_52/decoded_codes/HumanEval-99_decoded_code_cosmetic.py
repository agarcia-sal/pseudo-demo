from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def trim_trailing_zeros(str_val: str) -> str:
        if str_val.count('.') != 1:
            return str_val

        def recursive_trim(s: str) -> str:
            if len(s) == 0 or s[-1] != '0':
                return s
            return recursive_trim(s[:-1])

        return recursive_trim(str_val)

    temp_str: str = trim_trailing_zeros(value)
    try:
        float_num: float = float(temp_str)
    except ValueError:
        # If conversion fails, return 0 as a safe default per determine_result logic
        return 0

    def determine_result(s: str, number: float) -> int:
        if s[-2:] == '.5':
            return ceil(number) if number > 0 else floor(number)
        if len(s) > 0:
            return round(number)
        return 0

    return determine_result(temp_str, float_num)