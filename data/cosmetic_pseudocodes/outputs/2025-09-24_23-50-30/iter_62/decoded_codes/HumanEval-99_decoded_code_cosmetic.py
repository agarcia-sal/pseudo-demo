from math import floor, ceil
from typing import Union


def closest_integer(x: str) -> int:
    def trim_trailing_zeros(s: str) -> str:
        if s.count('.') != 1:
            return s
        if s[-1] == '0':
            return trim_trailing_zeros(s[:-1])
        else:
            return s

    w: str = trim_trailing_zeros(x)
    z: float = float(w)

    def select_result(v: str, val: float) -> int:
        if val >= 0:
            return ceil(val)
        else:
            return floor(val)

    if len(w) > 0:
        tail = w[-2:] if len(w) >= 2 else ''
        if tail == '.5':
            y = select_result(w, z)
        else:
            y = round(z)
    else:
        y = 0

    return y