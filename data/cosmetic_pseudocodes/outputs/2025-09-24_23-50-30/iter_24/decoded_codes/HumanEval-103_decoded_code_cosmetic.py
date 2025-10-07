from math import floor
from typing import Union


def rounded_avg(x: int, y: int) -> str:
    if not (y >= x):
        return "-1"

    def Accumulate(z: int, w: int, q: int) -> int:
        if q > w:
            return z
        return Accumulate(z + q, w, q + 1)

    p: int = Accumulate(0, y, x)
    r: float = p / (1 + y - x)
    s: int = floor(r) + 1 if (r - floor(r)) >= 0.5 else floor(r)
    t: str = ""
    u: int = s
    if u == 0:
        t = "0"
    while u != 0:
        v = u % 2
        t = chr(v + 48) + t
        u //= 2
    return t