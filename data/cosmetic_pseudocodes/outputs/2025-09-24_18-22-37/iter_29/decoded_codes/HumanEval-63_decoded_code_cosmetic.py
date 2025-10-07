from typing import Literal

def fibfib(num_x: int) -> int:
    if num_x == 0 or num_x == 1:
        return 0
    if num_x == 2:
        return 1
    a: int = num_x - 1
    b: int = num_x - 2
    c: int = num_x - 3
    res1: int = fibfib(a)
    res2: int = fibfib(b)
    res3: int = fibfib(c)
    result: int = res1 + res2 + res3
    return result