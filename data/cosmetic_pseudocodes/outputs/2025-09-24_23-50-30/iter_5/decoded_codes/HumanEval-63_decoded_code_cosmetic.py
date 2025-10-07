from functools import cache

@cache
def fibfib(x: int) -> int:
    if x == 0 or x == 1:
        return 0
    if x == 2:
        return 1
    return fibfib(x - 3) + fibfib(x - 2) + fibfib(x - 1)