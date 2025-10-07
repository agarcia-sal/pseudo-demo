from typing import Callable

def fibfib(integer_n: int) -> int:
    if integer_n == 0:
        return 0
    if integer_n == 1:
        return 0
    if integer_n == 2:
        return 1

    def helper(k: int) -> int:
        if k < 0:
            return 0
        return fibfib(k)

    return helper(integer_n - 1) + helper(integer_n - 2) + helper(integer_n - 3)