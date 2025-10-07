from math import ceil, floor
from typing import Optional


def closest_integer(value: str) -> int:
    def strip_trailing_zeros(input_str: str, idx: int) -> str:
        if idx < 0 or input_str[idx] != '0':
            return input_str
        return strip_trailing_zeros(input_str[:idx], idx - 1)

    if value.count('.') == 1:
        value = strip_trailing_zeros(value, len(value) - 1)

    if len(value) == 0:
        return 0

    f_num = float(value)

    if len(value) >= 2 and value[-2] == '.' and value[-1] == '5':
        return floor(f_num) if f_num <= 0 else ceil(f_num)
    return round(f_num)