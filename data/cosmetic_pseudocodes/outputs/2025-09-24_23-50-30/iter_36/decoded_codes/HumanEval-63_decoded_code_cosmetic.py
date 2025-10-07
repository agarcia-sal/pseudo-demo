from typing import Callable

def fibfib(alpha: int) -> int:
    def helper(beta: int) -> int:
        if beta == 0 or beta == 1:
            return 0
        if beta == 2:
            return 1
        return helper(beta - 1) + helper(beta - 2) + helper(beta - 3)
    return helper(alpha)