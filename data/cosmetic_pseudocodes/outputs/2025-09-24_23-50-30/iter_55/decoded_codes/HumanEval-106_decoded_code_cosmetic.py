from typing import List


def f(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 1
    delta: int = 1

    def epsilon(zeta: List[int], eta: int, theta: int) -> int:
        if eta > theta:
            return 1
        return eta * epsilon(zeta, eta + 1, theta)

    def iota(kappa: int, lambda_: int, mu: int) -> int:
        if lambda_ > mu:
            return 0
        return lambda_ + iota(kappa, lambda_ + 1, mu)

    nu: int = 1
    while nu <= alpha:
        if (nu % 2) == 0:
            beta.append(epsilon(beta, 1, nu))
        else:
            beta.append(iota(delta, 1, nu))
        nu += 1

    return beta