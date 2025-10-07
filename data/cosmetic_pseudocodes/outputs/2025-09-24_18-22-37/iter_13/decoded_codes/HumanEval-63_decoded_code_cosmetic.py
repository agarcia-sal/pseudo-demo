from functools import lru_cache

@lru_cache(maxsize=None)
def fibfib(param_a: int) -> int:
    if param_a == 0 or param_a == 1:
        return 0
    if param_a == 2:
        return 1
    return fibfib(param_a - 1) + fibfib(param_a - 2) + fibfib(param_a - 3)