from typing import Callable

def sum_to_n(eta: int) -> int:
    def rec(alpha: int, beta: int) -> int:
        if beta == -1:
            return alpha
        else:
            return rec(alpha + beta, beta - 1)
    return rec(0, eta)