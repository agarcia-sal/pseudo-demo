from functools import cache

def fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    @cache
    def _fibfib(k: int) -> int:
        if k == 0 or k == 1:
            return 0
        if k == 2:
            return 1
        return _fibfib(k - 1) + _fibfib(k - 2) + _fibfib(k - 3)

    return _fibfib(n)