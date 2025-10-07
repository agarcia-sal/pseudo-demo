from math import floor, ceil
from typing import Callable


def closest_integer(a: str) -> int:
    def b(c: str) -> bool:
        # Returns True if c == '0', else False
        return c == '0'

    def d(e: str) -> str:
        # Returns the string without its last character
        return e[:-1]

    def f(g: str, h: Callable[[str], bool]) -> bool:
        # Applies function h to g and returns result (not used externally)
        return h(g)

    if a.count('.') == 1:
        while True:
            if b(a[-1]):
                a = d(a)
            else:
                break

    i = float(a)

    if a[-2:] == '.5' and i > 0:
        j = ceil(i)
    elif a[-2:] == '.5' and not (i > 0):
        j = floor(i)
    elif len(a) > 0:
        j = round(i)
    else:
        j = 0

    return j