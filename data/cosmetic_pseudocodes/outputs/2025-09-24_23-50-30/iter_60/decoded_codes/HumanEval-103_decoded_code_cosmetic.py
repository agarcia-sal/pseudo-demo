from math import floor, ceil
from typing import Union


def rounded_avg(p: int, q: int) -> str:
    return helper_range_sum(p, q, p, 0)


def helper_range_sum(a: int, b: int, c: int, d: int) -> str:
    if c > b:
        e = d / (b - a + 1)
        f: int = ceil(e) if (e >= 0 and (e - floor(e)) >= 0.5) else floor(e)
        g: str = bin(f)[2:] if f >= 0 else '-' + bin(-f)[2:]
        return g
    else:
        return helper_range_sum(a, b, c + 1, d + c)