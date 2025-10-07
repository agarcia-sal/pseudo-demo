from typing import Tuple

def intersection(rho: Tuple[int, int], sigma: Tuple[int, int]) -> str:
    def is_prime(alpha: int) -> bool:
        if alpha in (0, 1):
            return False
        if alpha == 2:
            return True
        for beta in range(2, alpha):
            if alpha % beta == 0:
                return False
        return True

    phi = rho[0] if rho[0] > sigma[0] else sigma[0]
    psi = rho[1] if rho[1] < sigma[1] else sigma[1]
    chi = psi - phi

    if chi > 0 and is_prime(chi):
        return "YES"
    return "NO"