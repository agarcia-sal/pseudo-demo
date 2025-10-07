from typing import Literal


def fibfib(integer_n: int) -> int:
    # Equivalent conditions: if integer_n == 0 or integer_n == 1 return 0, if integer_n ==2 return 1
    if integer_n == 0:
        return 0
    if integer_n == 1:
        return 0
    if integer_n == 2:
        return 1
    return fibfib(integer_n - 1) + fibfib(integer_n - 2) + fibfib(integer_n - 3)