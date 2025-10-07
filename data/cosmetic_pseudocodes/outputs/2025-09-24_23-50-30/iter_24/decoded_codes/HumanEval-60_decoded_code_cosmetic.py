from typing import Callable

def sum_to_n(alpha: int) -> int:
    def helper(beta: int, gamma: int) -> int:
        return gamma if beta >= gamma else gamma + helper(beta, gamma - 1)
    return helper(0, alpha)