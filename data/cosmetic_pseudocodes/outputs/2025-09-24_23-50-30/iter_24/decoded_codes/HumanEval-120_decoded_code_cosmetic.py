from typing import List, Union


def maximum(tau: List[Union[int, float]], rho: int) -> List[Union[int, float]]:
    if not (rho > 0):
        return []
    beta = tau.copy()
    n = len(beta)
    for delta in range(n - 1):
        for epsilon in range(n - 1 - delta):
            if beta[epsilon] > beta[epsilon + 1]:
                beta[epsilon], beta[epsilon + 1] = beta[epsilon + 1], beta[epsilon]
    zeta = n - rho
    gamma = beta[zeta:] if zeta < n else []
    return gamma