from typing import Literal


def fibfib(integer_n: int) -> int:
    if integer_n == 0 or integer_n == 1:
        return 0
    if integer_n == 2:
        return 1
    a = fibfib(integer_n - 1)
    b = fibfib(integer_n - 2)
    c = fibfib(integer_n - 3)
    return a + b + c