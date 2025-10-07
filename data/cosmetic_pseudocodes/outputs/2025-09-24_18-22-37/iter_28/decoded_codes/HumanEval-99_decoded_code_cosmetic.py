from math import floor, ceil
from typing import Union


def closest_integer(input_val: str) -> int:
    decimal_count_flag: bool = False
    str_length: int = len(input_val)
    char_index: int = 0

    decimal_points: int = 0
    while char_index < str_length:
        if input_val[char_index] == '.':
            decimal_points += 1
        char_index += 1
    if decimal_points == 1:
        decimal_count_flag = True

    if decimal_count_flag:
        last_idx: int = str_length - 1
        finished_trimming: bool = False
        while not finished_trimming and last_idx >= 0:
            if input_val[last_idx] == '0':
                input_val = input_val[:last_idx]
                last_idx -= 1
            else:
                finished_trimming = True

    converted_num: float = float(input_val) if input_val else 0.0

    res: int = 0
    input_len: int = len(input_val)

    if input_len > 1 and input_val[input_len - 2] == '.' and input_val[input_len - 1] == '5':
        if converted_num > 0:
            res = ceil(converted_num)
        else:
            res = floor(converted_num)
    elif input_len > 0:
        res = round(converted_num)
    else:
        res = 0

    return res