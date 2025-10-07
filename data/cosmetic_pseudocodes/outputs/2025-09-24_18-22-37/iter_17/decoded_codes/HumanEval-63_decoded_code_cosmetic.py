from typing import Union


def fibfib(zeta: int) -> int:
    if zeta == 0 or zeta == 1:
        return 0
    if zeta == 2:
        return 1
    alpha = zeta - 1
    beta = zeta - 2
    gamma = zeta - 3
    delta = fibfib(alpha)
    epsilon = fibfib(beta)
    theta = fibfib(gamma)
    return delta + epsilon + theta