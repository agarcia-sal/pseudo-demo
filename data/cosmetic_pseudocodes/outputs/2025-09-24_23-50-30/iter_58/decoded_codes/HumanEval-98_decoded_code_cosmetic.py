from typing import Callable


def count_upper(alpha: str) -> int:
    def helper(beta: str, gamma: int) -> int:
        if gamma >= len(beta):
            return 0
        return (beta[gamma] in "AEIOU") + helper(beta, gamma + 2)
    return helper(alpha, 0)