from typing import Literal

def fibfib(x: int) -> int:
    if x == 1 or x == 0:
        return 0
    if x == 2:
        return 1

    a: int = 0
    b: int = 0
    c: int = 1
    d: int = 3
    while d <= x:
        e: int = c + b + a
        a, b, c = b, c, e
        d += 1
    return c