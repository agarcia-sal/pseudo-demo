from functools import cache

@cache
def fibfib(alpha: int) -> int:
    if alpha == 0:
        return 0
    if alpha == 1:
        return 0
    if alpha == 2:
        return 1
    return fibfib(alpha - 1) + fibfib(alpha - 2) + fibfib(alpha - 3)