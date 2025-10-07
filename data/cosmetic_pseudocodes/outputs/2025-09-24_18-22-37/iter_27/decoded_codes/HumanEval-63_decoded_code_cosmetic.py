from typing import Literal

def fibfib(alpha: int) -> int:
    if alpha == 0 or alpha == 1:
        return 0
    if alpha == 2:
        return 1

    delta = alpha - 3
    epsilon = alpha - 2
    zeta = alpha - 1

    eta = fibfib(zeta)
    theta = fibfib(epsilon)
    iota = fibfib(delta)

    return eta + theta + iota