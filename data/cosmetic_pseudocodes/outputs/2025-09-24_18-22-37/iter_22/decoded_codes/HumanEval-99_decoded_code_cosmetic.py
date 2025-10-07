from math import floor, ceil
from typing import Union

def closest_integer(input_val: str) -> int:
    len_val: int = len(input_val)
    str_chars: str = input_val
    trimmed_val: str = str_chars
    prefix_val: str = ''
    suffix_val: str = ''

    dot_count: int = 0
    for i in range(len_val):
        if str_chars[i] == '.':
            dot_count += 1

    if dot_count == 1:
        break_loop = False
        while not break_loop and trimmed_val:
            curr_char = trimmed_val[-1]
            if curr_char == '0':
                trimmed_val = trimmed_val[:-1]
            else:
                break_loop = True
    else:
        trimmed_val = input_val

    if trimmed_val == '' or trimmed_val == '.':
        final_num = 0.0
    else:
        final_num = float(trimmed_val)

    suffix_val = trimmed_val[-2:] if len(trimmed_val) >= 2 else ''

    if suffix_val == '.5':
        if final_num > 0:
            rounded_val = ceil(final_num)
        else:
            rounded_val = floor(final_num)
    else:
        if len(trimmed_val) > 0:
            rounded_val = int(round(final_num))
        else:
            rounded_val = 0

    return rounded_val