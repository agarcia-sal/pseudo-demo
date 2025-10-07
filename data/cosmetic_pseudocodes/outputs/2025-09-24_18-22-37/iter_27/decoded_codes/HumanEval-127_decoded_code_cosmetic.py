from typing import Sequence


def intersection(alpha: Sequence[int], beta: Sequence[int]) -> str:
    def is_prime(zeta: int) -> bool:
        if zeta <= 1:
            return False
        if zeta == 2:
            return True
        for xi in range(2, zeta):
            if zeta % xi == 0:
                return False
        return True

    sigma: int = alpha[0] if alpha[0] >= beta[0] else beta[0]
    tau: int = alpha[1] if alpha[1] <= beta[1] else beta[1]
    rho: int = tau - sigma

    if rho > 0 and is_prime(rho):
        return "YES"
    return "NO"