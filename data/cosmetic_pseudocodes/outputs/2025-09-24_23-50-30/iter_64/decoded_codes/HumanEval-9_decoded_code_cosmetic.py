from typing import List, Optional

def rolling_max(alpha: List[float]) -> List[float]:
    rho: List[float] = []
    mu: Optional[float] = None

    iota: int = 0
    while iota < len(alpha):
        omega: float = alpha[iota]

        if mu is None:
            mu = omega
        else:
            mu = mu if mu >= omega else omega

        rho.append(mu)
        iota += 1

    return rho