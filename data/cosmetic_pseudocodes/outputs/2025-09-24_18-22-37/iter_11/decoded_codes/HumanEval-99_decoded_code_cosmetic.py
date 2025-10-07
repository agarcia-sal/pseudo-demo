from math import floor, ceil
from typing import Union


def closest_integer(input_str: str) -> int:
    decimal_count: int = 0
    for ch in input_str:
        if ch == '.':
            decimal_count += 1

    if decimal_count == 1:
        temp_str: str = input_str
        str_len: int = len(temp_str)
        while str_len > 0:
            curr_char: str = temp_str[str_len - 1]
            if curr_char != '0':
                break
            temp_str = temp_str[:str_len - 1]
            str_len -= 1
        input_str = temp_str

    number_val: float = float(input_str) if input_str else 0.0

    last_two_chars: str = ''
    if len(input_str) >= 2:
        last_two_chars = input_str[-2] + input_str[-1]

    str_len = len(input_str)

    if last_two_chars == '.5':
        if number_val > 0.0:
            rounded_val: int = ceil(number_val)
        else:
            rounded_val = floor(number_val)
    else:
        if str_len > 0:
            rounded_val = round(number_val)
        else:
            rounded_val = 0

    return rounded_val