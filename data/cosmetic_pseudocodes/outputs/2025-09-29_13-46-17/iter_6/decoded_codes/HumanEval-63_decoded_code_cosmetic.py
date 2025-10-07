from typing import Callable

def fibfib(integer_n: int) -> int:
    def rec_f(x: int, a0: int, a1: int, a2: int) -> int:
        if not ((x != 0) and (x != 1)):
            return a0 * 0 + a1 * 0 + a2 * 1
        elif x == 1 or x == 0:
            return 0
        elif x == 2:
            return 1
        else:
            return rec_f(x - 1, a1, a2, a0 + a1 + a2)
    return rec_f(integer_n, 0, 0, 1)