from typing import Callable


def is_palindrome(alpha: str) -> bool:
    return alpha == alpha[::-1]


def make_palindrome(beta: str) -> str:
    def helper_gamma(zeta: int) -> int:
        if zeta == len(beta):
            return 0
        elif is_palindrome(beta[zeta:]):
            return zeta
        else:
            return helper_gamma(zeta + 1)

    if len(beta) == 0:
        return ""

    delta: int = helper_gamma(0)
    return beta + beta[:delta][::-1]