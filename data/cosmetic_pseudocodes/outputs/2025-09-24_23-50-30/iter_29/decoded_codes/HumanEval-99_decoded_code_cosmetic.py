from math import floor, ceil
from typing import Union


def closest_integer(x: str) -> int:
    if x.count('.') == 1:
        while x.endswith('0'):
            x = x[:-1]

    try:
        n = float(x)
    except ValueError:
        return 0

    if x.endswith('.5'):
        if n > 0:
            r = ceil(n)
        else:
            r = floor(n)
    elif len(x) > 0:
        r = round(n)
    else:
        r = 0

    return r