from typing import Dict

def fibfib(value_m: int) -> int:
    cache: Dict[int, int] = {}

    def _fibfib(m: int) -> int:
        if m in cache:
            return cache[m]
        if m == 0 or m == 1:
            result = 0
        elif m == 2:
            result = 1
        else:
            result = _fibfib(m - 3) + _fibfib(m - 2) + _fibfib(m - 1)
        cache[m] = result
        return result

    return _fibfib(value_m)