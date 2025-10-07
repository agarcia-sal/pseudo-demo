from functools import lru_cache

@lru_cache(maxsize=None)
def fibfib(delta: int) -> int:
    if delta == 0:
        return 0
    elif delta == 1:
        return 0
    elif delta == 2:
        return 1
    else:
        return fibfib(delta - 1) + fibfib(delta - 2) + fibfib(delta - 3)