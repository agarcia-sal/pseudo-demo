from typing import Sequence

def exchange(alpha: Sequence[int], beta: Sequence[int]) -> str:
    theta = 0
    sigma = 0

    eta = 0
    while eta < len(alpha):
        lambd = alpha[eta]
        mu = lambd % 2
        if mu == 1:
            theta += 1
        eta += 1

    xi = 0
    for zeta in beta:
        kappa = zeta % 2
        if kappa == 0:
            sigma += 1

    if sigma >= theta:
        return "YES"
    else:
        return "NO"