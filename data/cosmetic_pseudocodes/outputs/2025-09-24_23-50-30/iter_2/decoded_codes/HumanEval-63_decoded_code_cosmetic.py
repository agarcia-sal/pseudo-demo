from typing import Literal

def fibfib(n: int) -> int:
    if not (n > 2):
        if n in (0, 1):
            return 0
        if n == 2:
            return 1
    return fibfib(n - 3) + fibfib(n - 2) + fibfib(n - 1)