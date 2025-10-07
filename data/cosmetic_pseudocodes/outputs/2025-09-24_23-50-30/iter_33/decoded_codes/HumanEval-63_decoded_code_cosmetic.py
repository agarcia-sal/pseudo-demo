from functools import lru_cache

@lru_cache(None)
def fibfib(index_x: int) -> int:
    if index_x == 0:
        return 0
    if index_x == 1:
        return 0
    if index_x == 2:
        return 1
    return fibfib(index_x - 1) + fibfib(index_x - 2) + fibfib(index_x - 3)