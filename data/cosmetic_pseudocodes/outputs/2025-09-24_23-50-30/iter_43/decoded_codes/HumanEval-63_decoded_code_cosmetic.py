from typing import Literal

def fibfib(integer_p: int) -> int:
    q: int = 0
    r: int = 0
    s: int = 1
    t: int = 3
    while t <= integer_p:
        u: int = s + r + q
        q = r
        r = s
        s = u
        t += 1
    if integer_p in (0, 1):
        return 0
    if integer_p == 2:
        return 1
    return s