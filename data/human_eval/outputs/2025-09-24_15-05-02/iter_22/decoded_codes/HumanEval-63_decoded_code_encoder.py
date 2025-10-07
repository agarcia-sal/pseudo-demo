from functools import lru_cache

def fibfib(position: int) -> int:
    if position == 0:
        return 0
    if position == 1:
        return 0
    if position == 2:
        return 1

    @lru_cache(maxsize=None)
    def _fibfib_cached(pos: int) -> int:
        if pos == 0:
            return 0
        if pos == 1:
            return 0
        if pos == 2:
            return 1
        return _fibfib_cached(pos - 1) + _fibfib_cached(pos - 2) + _fibfib_cached(pos - 3)

    return _fibfib_cached(position)