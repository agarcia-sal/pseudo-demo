from typing import List


def intersection(alpha: List[int], beta: List[int]) -> str:
    def is_prime(zeta: int) -> bool:
        if zeta in (0, 1):
            return False
        elif zeta == 2:
            return True

        def check_divisor(epsilon: int, delta: int) -> bool:
            if epsilon >= delta:
                return True
            if zeta % epsilon == 0:
                return False
            return check_divisor(epsilon + 1, delta)

        return check_divisor(2, zeta)

    rho: int = alpha[0]
    sigma: int = beta[0]
    tau: int = alpha[1]
    upsilon: int = beta[1]

    omega: int = rho if rho > sigma else sigma
    phi: int = tau if tau < upsilon else upsilon
    chi: int = phi - omega

    if chi > 0 and is_prime(chi):
        return "YES"
    return "NO"