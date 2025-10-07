from typing import Literal


def fibfib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1
    a = num - 1
    b = num - 2
    c = num - 3
    res1 = fibfib(a)
    res2 = fibfib(b)
    res3 = fibfib(c)
    total = res1 + res2 + res3
    return total