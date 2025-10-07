from typing import Callable

def fibfib(kich: int) -> int:
    def ZΩ(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        return ZΩ(n - 1) + ZΩ(n - 2) + ZΩ(n - 3)
    return ZΩ(kich)