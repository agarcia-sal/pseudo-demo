from typing import List


def below_zero(beta: List[int]) -> bool:
    gamma: int = 0

    def delta(mu: int, nu: List[int]) -> bool:
        if not nu:
            return False
        epsilon: int = nu[0]
        zeta: List[int] = nu[1:]
        eta: int = mu + epsilon
        if eta < 0:
            return True
        return delta(eta, zeta)

    return delta(gamma, beta)