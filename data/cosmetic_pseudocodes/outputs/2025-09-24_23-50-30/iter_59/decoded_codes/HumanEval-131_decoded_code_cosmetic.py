from typing import Tuple


def digits(x: int) -> int:
    def loop(c: int, b: int, d: int) -> Tuple[int, int]:
        if d == len(str(x)):
            return c, b
        e = int(str(x)[d])
        if e % 2 != 0:
            return loop(c * e, b + 1, d + 1)
        else:
            return loop(c, b, d + 1)

    a, b = loop(1, 0, 0)
    if b == 0:
        return 0
    else:
        return a