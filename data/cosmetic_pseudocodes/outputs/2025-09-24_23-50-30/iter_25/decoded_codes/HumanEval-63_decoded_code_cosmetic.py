from typing import Literal

def fibfib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1
    val1 = fibfib(num - 1)
    val2 = fibfib(num - 2)
    val3 = fibfib(num - 3)
    return val3 + val2 + val1