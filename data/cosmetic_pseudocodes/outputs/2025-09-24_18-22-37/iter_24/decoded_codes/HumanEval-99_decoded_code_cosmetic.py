from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    first_flag: bool = False
    second_flag: bool = False
    temp_num: float = 0.0
    temp_result: int = 0
    idx: int = 0
    last_char: str = ''
    last_two_chars: str = ''
    len_value: int = 0
    dot_count: int = 0
    new_value: str = value

    # Count how many '.' characters are in new_value
    dot_count = 0
    idx = 0
    while idx < len(new_value):
        if new_value[idx] == '.':
            dot_count += 1
        idx += 1

    first_flag = dot_count == 1

    if first_flag:
        # Trim trailing '0's after decimal point
        while True:
            len_value = len(new_value)
            if len_value == 0:
                break
            last_char = new_value[len_value - 1]
            if last_char == '0':
                new_value = new_value[:len_value - 1]
            else:
                break

    temp_num = float(new_value) if new_value else 0.0

    len_value = len(new_value)
    if len_value >= 2:
        last_two_chars = new_value[len_value - 2] + new_value[len_value - 1]
    else:
        last_two_chars = ''

    second_flag = last_two_chars == '.5'

    if second_flag:
        if temp_num > 0:
            temp_result = ceil(temp_num)
        else:
            temp_result = floor(temp_num)
    else:
        if len_value > 0:
            temp_result = round(temp_num)
        else:
            temp_result = 0

    return temp_result