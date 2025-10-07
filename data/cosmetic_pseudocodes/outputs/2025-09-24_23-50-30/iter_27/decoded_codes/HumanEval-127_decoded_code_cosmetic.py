from typing import Tuple

def intersection(alpha: Tuple[int, int], beta: Tuple[int, int]) -> str:
    def is_prime(zeta: int) -> bool:
        if zeta == 0 or zeta == 1:
            return False
        if zeta == 2:
            return True
        for kappa in range(2, zeta):
            if zeta % kappa == 0:
                return False
        return True

    phi: int = alpha[0] if alpha[0] >= beta[0] else beta[0]
    psi: int = alpha[1] if alpha[1] <= beta[1] else beta[1]
    delta: int = psi - phi
    if delta > 0 and is_prime(delta):
        return "YES"
    else:
        return "NO"