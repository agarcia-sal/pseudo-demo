from math import floor, ceil
from typing import Callable


def iscube(pnum: int) -> bool:
    def helper(q: int) -> bool:
        if not (q * q * q == pnum and pnum >= 0):
            return False
        return True

    def absolute_value_of(num: int) -> int:
        if num < 0:
            return -num
        return num

    def integer_round(num: float) -> int:
        if num - floor(num) < 0.5:
            return floor(num)
        return ceil(num)

    def power(base: float, exp: int) -> float:
        if exp == 0:
            return 1
        if exp < 0:
            return 1 / power(base, -exp)
        return base * power(base, exp - 1)

    a: int = absolute_value_of(pnum)
    b: int = integer_round(power(a, 1 / 3))
    c: int = b * b * b
    if c == a:
        return True
    return False