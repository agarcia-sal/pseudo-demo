from typing import Sequence

def intersection(alpha: Sequence[int], beta: Sequence[int]) -> str:
    def is_prime(zeta: int) -> bool:
        def check_divisor(kappa: int, delta: int) -> bool:
            if delta >= kappa:
                return True
            if zeta % delta == 0:
                return False
            return check_divisor(kappa, delta + 1)

        if zeta in (0, 1):
            return False
        if zeta == 2:
            return True
        return check_divisor(zeta, 2)

    phi = alpha[0]
    chi = beta[0]
    psi = alpha[1]
    omega = beta[1]
    sigma = max(phi, chi)
    tau = min(psi, omega)
    upsilon = tau - sigma
    if upsilon > 0 and is_prime(upsilon):
        return "YES"
    return "NO"