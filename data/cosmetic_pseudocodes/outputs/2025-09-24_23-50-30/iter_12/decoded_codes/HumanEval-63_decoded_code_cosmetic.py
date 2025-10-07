from typing import Callable


def fibfib(integer_n: int) -> int:
    if integer_n == 0 or integer_n == 1:
        return 0
    if integer_n == 2:
        return 1

    def helper(current: int) -> int:
        if current <= 2:
            return 0 if current in (0, 1) else 1
        return helper(current - 1) + helper(current - 2) + helper(current - 3)

    return helper(integer_n)