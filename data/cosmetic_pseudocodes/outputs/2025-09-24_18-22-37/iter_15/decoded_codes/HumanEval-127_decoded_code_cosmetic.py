from typing import Sequence


def intersection(alpha: Sequence[int], beta: Sequence[int]) -> str:
    def is_prime(phi: int) -> bool:
        psi = phi
        if psi == 0 or psi == 1:
            return False
        if psi == 2:
            return True
        zeta = 2
        while zeta < psi:
            if phi % zeta == 0:
                return False
            zeta += 1
        return True

    tau = alpha[0]
    upsilon = beta[0]
    chi = alpha[1]
    omega = beta[1]

    mu = tau if tau > upsilon else upsilon
    nu = chi if chi < omega else omega

    sigma = nu - mu

    if sigma > 0 and is_prime(sigma):
        return "YES"
    return "NO"