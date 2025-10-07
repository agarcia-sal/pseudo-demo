from typing import Callable


def fibfib(integer_n: int) -> int:
    if integer_n in (0, 1):
        return 0
    if integer_n == 2:
        return 1

    def helper(index: int) -> int:
        if index < 0:
            return 0
        if index == 0 or index == 1:
            return 0
        if index == 2:
            return 1
        return helper(index - 1) + helper(index - 2) + helper(index - 3)

    return helper(integer_n)