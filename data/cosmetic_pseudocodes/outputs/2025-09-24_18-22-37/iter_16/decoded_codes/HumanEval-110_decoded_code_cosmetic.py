from typing import Sequence, Union


def exchange(alpha: Sequence[int], beta: Sequence[int]) -> str:
    gamma: int = 0
    delta: int = 0
    zeta: int = 0
    while zeta < len(alpha):
        kappa: int = alpha[zeta]
        if kappa % 2 == 1:
            gamma += 1
        zeta += 1
    eta: int = 0
    while eta < len(beta):
        theta: int = beta[eta]
        if theta % 2 == 0:
            delta += 1
        eta += 1
    if delta >= gamma:
        return "YES"
    else:
        return "NO"