from typing import Callable

def fibfib(x1: int) -> int:
    if x1 < 1:
        return 0
    if x1 < 2:
        return 0
    if x1 < 3:
        return 1

    def helper(x2: int, x3: int, x4: int, acc: int) -> int:
        if x4 > x2:
            return acc
        return helper(
            x2,
            x3,
            x4 + 1,
            acc + fibfib(x4 - 1) + fibfib(x4 - 2) + fibfib(x4 - 3)
        )
    # According to the given pseudocode, the call to helper is not used or returned
    return fibfib(x1 - 1) + fibfib(x1 - 2) + fibfib(x1 - 3)