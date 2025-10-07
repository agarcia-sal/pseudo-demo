from typing import Callable


def concatenate(alpha: str) -> str:
    def recurse(beta: str, gamma: int) -> str:
        if gamma == 0:
            return beta
        else:
            return recurse(beta + alpha[gamma - 1], gamma - 1)
    return recurse("", len(alpha))