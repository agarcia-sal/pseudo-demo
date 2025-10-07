from math import floor, ceil
from typing import Union

def closest_integer(parameter1: str) -> int:
    count_dots: int = 0
    index_tracker: int = 0
    while index_tracker < len(parameter1):
        if parameter1[index_tracker] == '.':
            count_dots += 1
        index_tracker += 1

    if count_dots == 1:
        idx_last: int = len(parameter1) - 1
        while idx_last >= 0 and parameter1[idx_last] == '0':
            parameter1 = parameter1[:idx_last]
            idx_last -= 1

    floating_value: float = float(parameter1) if parameter1 else 0.0

    tail_two: str = ""
    if len(parameter1) >= 2:
        tail_two = parameter1[-2] + parameter1[-1]

    if tail_two == '.5':
        if floating_value > 0.0:
            return ceil(floating_value)
        else:
            return floor(floating_value)
    else:
        if len(parameter1) > 0:
            return round(floating_value)
        else:
            return 0