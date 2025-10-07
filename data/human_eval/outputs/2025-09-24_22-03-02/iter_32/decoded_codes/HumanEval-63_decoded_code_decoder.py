from functools import lru_cache

@lru_cache(None)
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = fibfib(n - 1)
    b = fibfib(n - 2)
    c = fibfib(n - 3)
    result = a + b + c
    return result