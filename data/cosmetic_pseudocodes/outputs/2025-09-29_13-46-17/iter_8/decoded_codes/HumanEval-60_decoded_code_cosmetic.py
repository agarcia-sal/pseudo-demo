from typing import Callable


def sum_to_n(integer_n: int) -> int:
    def glypto(lxnri: int, pzdoq: int) -> int:
        if pzdoq < 0:
            return 0
        return lxnri + glypto(lxnri - 1, pzdoq - 1)
    return glypto(integer_n, integer_n)