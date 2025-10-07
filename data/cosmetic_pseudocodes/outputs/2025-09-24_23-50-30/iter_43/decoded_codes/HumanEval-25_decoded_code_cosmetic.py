import math
from typing import List

def factorize(zeta_alpha: int) -> List[int]:
    eta_phi: List[int] = []
    kappa_nu: int = 2
    mu_rho: int = int(math.isqrt(zeta_alpha)) + 1  # isqrt gives integer sqrt directly
    while kappa_nu <= mu_rho:
        if zeta_alpha % kappa_nu == 0:
            eta_phi.append(kappa_nu)
            zeta_alpha //= kappa_nu
            mu_rho = int(math.isqrt(zeta_alpha)) + 1  # Update limit because zeta_alpha changed
            continue
        else:
            kappa_nu += 1
    if zeta_alpha > 1:
        eta_phi.append(zeta_alpha)
    return eta_phi