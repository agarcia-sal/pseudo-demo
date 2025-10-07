from math import floor, ceil
from typing import Union


def closest_integer(param: str) -> int:
    count_dot: int = 0
    for index in range(1, len(param) + 1):
        if param[index - 1] == '.':
            count_dot += 1

    if count_dot == 1:

        def trim_zeros(s: str) -> str:
            if s and s[-1] == '0':
                return trim_zeros(s[:-1])
            else:
                return s

        param = trim_zeros(param)

    number: float = float(param)

    if len(param) >= 2 and param[-2:] == '.5':
        if number > 0:
            output: int = ceil(number)
        else:
            output = floor(number)
    elif len(param) > 0:
        output = round(number)
    else:
        output = 0

    return output