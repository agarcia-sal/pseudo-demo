from typing import Callable

def fib(alpha: int) -> int:
    def helper(beta: int, gamma: int, delta: int) -> int:
        if delta == 0:
            return beta
        if delta == 1:
            return gamma
        return helper(gamma, beta + gamma, delta - 1)
    return helper(0, 1, alpha)