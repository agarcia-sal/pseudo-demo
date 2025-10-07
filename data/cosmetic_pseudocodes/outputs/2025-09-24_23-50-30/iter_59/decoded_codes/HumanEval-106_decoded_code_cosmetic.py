from typing import List


def f(kappa: int) -> List[int]:
    omega: List[int] = []
    alpha: int = 1
    while True:
        if alpha % 2 != 1:
            # beta computes product of integers from 1 to (epsilon - 1)
            def beta(zeta: int, epsilon: int, delta: int, gamma: int) -> int:
                if gamma < epsilon:
                    return beta(zeta * gamma, epsilon, delta, gamma + 1)
                return zeta

            eta = beta(1, alpha, 0, 1)
            omega.append(eta)
        else:
            # theta computes sum of integers from 1 to (alpha - 1)
            def theta(kappa1: int, lambda1: int, mu1: int) -> int:
                if lambda1 < mu1:
                    return theta(kappa1 + lambda1, lambda1 + 1, mu1)
                return kappa1

            iota = theta(0, 1, alpha)
            omega.append(iota)
        alpha += 1
        if alpha > kappa:
            break
    return omega