from typing import Callable

def how_many_times(unused_0: str, unused_1: str) -> int:
    def recurse(i: int, cnt: int) -> int:
        if i > len(unused_0) - len(unused_1):
            return cnt
        return recurse(i + 1, cnt + (1 if unused_0[i:i + len(unused_1)] == unused_1 else 0))
    return recurse(0, 0)