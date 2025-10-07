from typing import Literal


def fibfib(alpha: int) -> int:
    if alpha == 0 or alpha == 1:
        return 0
    if alpha == 2:
        return 1
    delta = alpha - 1
    epsilon = alpha - 2
    zeta = alpha - 3
    return fibfib(delta) + fibfib(epsilon) + fibfib(zeta)