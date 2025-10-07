from typing import Callable


def fibfib(unused_a: int) -> int:
    if unused_a == 0 or unused_a == 1:
        return 0
    if unused_a == 2:
        return 1

    temp_x = unused_a - 1
    temp_y = unused_a - 2
    temp_z = unused_a - 3

    result_x = fibfib.at(temp_x)
    result_y = fibfib.at(temp_y)
    result_z = fibfib.at(temp_z)

    sum_total = result_x + result_y + result_z
    return sum_total


# Attach the memoized version as fibfib.at to avoid recomputation
def _fibfib_at(n: int, cache={0: 0, 1: 0, 2: 1}) -> int:
    if n in cache:
        return cache[n]
    cache[n] = _fibfib_at(n - 1) + _fibfib_at(n - 2) + _fibfib_at(n - 3)
    return cache[n]


fibfib.at = _fibfib_at