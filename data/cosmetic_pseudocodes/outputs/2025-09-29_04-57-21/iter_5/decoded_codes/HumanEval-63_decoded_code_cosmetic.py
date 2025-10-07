from typing import Callable

def fibfib(alpha: int) -> int:
    if alpha == 0 or alpha == 1:
        return 0
    if alpha == 2:
        return 1

    def helper(beta: int) -> int:
        if beta >= 3:
            return helper(beta - 1) + helper(beta - 2) + helper(beta - 3)
        if beta == 0 or beta == 1:
            return 0
        else:
            return 1

    return helper(alpha)