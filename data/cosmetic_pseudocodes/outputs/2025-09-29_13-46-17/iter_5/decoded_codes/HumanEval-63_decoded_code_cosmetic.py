from typing import Callable

def fibfib(x: int) -> int:
    def helper(curr: int) -> int:
        if curr <= 1:
            return 0
        if curr == 2:
            return 1
        return helper(curr - 1) + helper(curr - 2) + helper(curr - 3)
    return helper(x)