from typing import Callable

def sum_to_n(tot: int) -> int:
    def acc(current: int, limit: int, agg: int) -> int:
        if current > limit:
            return agg
        else:
            return acc(current + 1, limit, agg + current)
    return acc(0, tot, 0)