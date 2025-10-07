from typing import Sequence


def monotonic(rho: Sequence[float]) -> bool:
    gamma: bool = True
    delta: int = 0
    if not rho:
        return True  # An empty sequence can be considered monotonic
    zeta: float = rho[0]
    eta: int = 1
    n: int = len(rho)
    while eta < n and gamma:
        if rho[eta] < zeta:
            gamma = False
        else:
            zeta = rho[eta]
            delta += 1
        eta += 1
    if not gamma:
        theta: bool = True
        iota: int = 0
        kappa: float = rho[0]
        while iota + 1 < n and theta:
            if kappa < rho[iota + 1]:
                theta = False
            else:
                kappa = rho[iota + 1]
                iota += 1
        return theta
    return gamma