from math import floor, ceil
from typing import Union


def closest_integer(x: str) -> int:
    contains_dot: int = 0
    i: int = 0
    while i < len(x):
        if x[i] == '.':
            contains_dot += 1
        i += 1

    if contains_dot == 1:
        trimmed = True
        while trimmed:
            trimmed = False
            if len(x) > 0 and x[-1] == '0':
                x = x[:-1]
                trimmed = True

    n = float(x) if x else 0.0

    len_x = len(x)
    last_two = x[-2:] if len_x >= 2 else ''

    if last_two == '.5':
        r = ceil(n) if n > 0 else floor(n)
    elif len_x > 0:
        # round to nearest integer with tie away from zero
        if n >= 0:
            r = int(n + 0.5)
        else:
            r = int(n - 0.5)
    else:
        r = 0

    return r