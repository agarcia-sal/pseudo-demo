from typing import Callable

def sum_to_n(s: int) -> int:
    def helper(t: int, u: int) -> int:
        if t > u:
            return 0
        else:
            return t + helper(t + 1, u)
    return helper(0, s)