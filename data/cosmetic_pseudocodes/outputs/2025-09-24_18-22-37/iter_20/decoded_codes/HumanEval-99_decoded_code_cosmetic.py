from math import floor, ceil
from typing import Union


def closest_integer(qwerty: str) -> int:
    xzxcz: int = 0
    str_len: int = len(qwerty)
    trimmed_value: str = qwerty

    temp_var1: int = 0
    trim_loop: bool = False
    output_result: int = 0

    temp_var1 = trimmed_value.count('.')

    if temp_var1 == 1:
        trim_loop = True

    while trim_loop:
        last_char = trimmed_value[-1]
        if last_char != '0':
            trim_loop = False
            break
        trimmed_value = trimmed_value[:-1]

    parsed_num: float = float(trimmed_value)

    last_two_chars: str = trimmed_value[-2:] if len(trimmed_value) >= 2 else ''

    if not (last_two_chars != '.5'):
        if parsed_num > 0:
            output_result = ceil(parsed_num)
        else:
            output_result = floor(parsed_num)
    else:
        if len(trimmed_value) > 0:
            output_result = int(parsed_num - (parsed_num % 1))

            temp_int: float = parsed_num - output_result
            if temp_int >= 0.5:
                output_result += 1
        else:
            output_result = 0

    return output_result