from math import floor, ceil
from typing import Union


def closest_integer(u: str) -> int:
    def truncate_zeroes(v: str, w: int) -> str:
        if w <= 0:
            return v
        if v[w] != '0':
            return v
        return truncate_zeroes(v[:w], w - 1)

    if '.' not in u:
        v = u
    else:
        v = truncate_zeroes(u, len(u) - 1)

    n = float(v)
    if v.endswith('.5'):
        if n > 0:
            r = ceil(n)
        else:
            r = floor(n)
    elif len(v) > 0:
        r = round(n)
    else:
        r = 0

    return r