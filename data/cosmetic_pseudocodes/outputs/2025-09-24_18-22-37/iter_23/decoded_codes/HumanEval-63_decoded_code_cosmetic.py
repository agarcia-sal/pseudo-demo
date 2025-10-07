from typing import Literal


def fibfib(alpha: int) -> int:
    if alpha == 0 or alpha == 1:
        return 0
    if alpha == 2:
        return 1

    beta: int = alpha - 1
    gamma: int = alpha - 2
    delta: int = alpha - 3  # 1 + 2 = 3
    epsilon: int = fibfib(beta)
    zeta: int = fibfib(gamma)
    eta: int = fibfib(delta)
    return epsilon + zeta + eta