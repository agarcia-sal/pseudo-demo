from typing import Callable

def fibfib(integer_n: int) -> int:
    def inner_fibfib(z: int) -> int:
        if z == 0:
            return 0
        if z == 1:
            return 0
        if z == 2:
            return 1
        return inner_fibfib(z - 1) + inner_fibfib(z - 2) + inner_fibfib(z - 3)
    return inner_fibfib(integer_n)