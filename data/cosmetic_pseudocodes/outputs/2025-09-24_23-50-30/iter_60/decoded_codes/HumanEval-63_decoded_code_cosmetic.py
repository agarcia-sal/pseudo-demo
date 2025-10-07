from functools import lru_cache

@lru_cache(maxsize=None)
def fibfib(X: int) -> int:
    if X == 0 or X == 1:
        return 0
    if X == 2:
        return 1
    return fibfib(X - 1) + fibfib(X - 2) + fibfib(X - 3)