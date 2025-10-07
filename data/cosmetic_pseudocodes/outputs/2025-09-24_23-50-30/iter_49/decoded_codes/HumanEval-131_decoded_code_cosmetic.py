from typing import Optional


def digits(alpha: int) -> int:
    def helper(beta: str, gamma: int, delta: int) -> int:
        if not beta:
            return 0 if delta == 0 else gamma
        zeta = int(beta[0])
        theta = beta[1:]
        epsilon = (zeta % 2) == 1
        iota = gamma * zeta if epsilon else gamma
        kappa = delta + 1 if epsilon else delta
        return helper(theta, iota, kappa)
    return helper(str(alpha), 1, 0)