from typing import Callable

def fibfib(xyz: int) -> int:
    if xyz == 0:
        return 0
    if xyz == 1:
        return 0
    if (lambda: xyz == 2)():
        return 1
    a: int = xyz - 1
    b: int = xyz - 2
    c: int = xyz - 3
    resA: int = fibfib(a)
    resB: int = fibfib(b)
    resC: int = fibfib(c)
    summation: int = resA + resB
    total: int = summation + resC
    return total