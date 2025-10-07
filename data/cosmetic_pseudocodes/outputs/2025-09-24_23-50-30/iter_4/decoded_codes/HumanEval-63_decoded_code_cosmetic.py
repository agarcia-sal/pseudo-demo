from functools import cache

@cache
def fibfib(n: int) -> int:
    if n in (0, 1):
        return 0
    if n == 2:
        return 1
    a = fibfib(n - 3)
    b = fibfib(n - 2)
    c = fibfib(n - 1)
    return a + b + c