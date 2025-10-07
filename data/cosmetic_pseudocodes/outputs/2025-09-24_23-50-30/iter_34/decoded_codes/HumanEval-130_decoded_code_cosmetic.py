from typing import List


def tri(omega: int) -> List[int]:
    if omega == 0:
        return [1]
    kappa: List[int] = [1, 3]

    def loop(delta: int, epsilon: List[int]) -> List[int]:
        if delta > omega:
            return epsilon
        zeta: bool = (delta % 2) == 0
        if zeta:
            rho: int = (delta // 2) + 1
            sigma = epsilon + [rho]
            return loop(delta + 1, sigma)
        else:
            tau: int = epsilon[delta - 1] + epsilon[delta - 2] + ((delta + 3) // 2)
            upsilon = epsilon + [tau]
            return loop(delta + 1, upsilon)

    return loop(2, kappa)