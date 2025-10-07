from typing import Callable

def sum_to_n(alpha: int) -> int:
    def recurse_omega(beta: int, gamma: int) -> int:
        if gamma == alpha + 1:
            return beta
        else:
            return recurse_omega(beta + gamma, gamma + 1)
    return recurse_omega(0, 0)