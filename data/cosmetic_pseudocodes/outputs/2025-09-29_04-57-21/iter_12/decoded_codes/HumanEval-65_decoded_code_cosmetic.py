from typing import Tuple


def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_val = str(integer_x)
    if integer_shift > len(str_val):
        return str_val[::-1]

    len_str = len(str_val)
    pivot = len_str - integer_shift

    tail_substring = str_val[pivot:]
    head_substring = str_val[:pivot]

    return tail_substring + head_substring