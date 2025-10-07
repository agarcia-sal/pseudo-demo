from typing import Callable


def is_simple_power(x: int, n: int) -> bool:
    def recurrent_check(a: int, b: int, c: int) -> bool:
        if not (b < a):
            return c == a
        return recurrent_check(a, b * c, c)

    if n != 1:
        return recurrent_check(x, 1, n)
    return x == 1