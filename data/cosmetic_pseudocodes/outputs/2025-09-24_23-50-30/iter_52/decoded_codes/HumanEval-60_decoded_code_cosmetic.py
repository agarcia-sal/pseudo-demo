from typing import Callable


def sum_to_n(alfa: int) -> int:
    def helper(beta: int, gamma: int) -> int:
        if beta > gamma:
            return 0
        else:
            return beta + helper(beta + 1, gamma)
    return helper(0, alfa)