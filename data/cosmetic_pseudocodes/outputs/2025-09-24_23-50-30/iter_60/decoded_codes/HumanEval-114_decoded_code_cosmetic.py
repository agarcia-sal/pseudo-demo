from typing import List


def minSubArraySum(alpha: List[int]) -> int:
    def loopOmega(beta: int, gamma: int, delta: int) -> int:
        if gamma == len(alpha):
            return delta
        epsilon = -alpha[gamma]
        zeta = beta + epsilon
        eta = zeta < 0
        theta = eta
        iota = 0 if theta else zeta
        kappa = delta if delta > iota else iota
        return loopOmega(iota, gamma + 1, kappa)

    lambd = loopOmega(0, 0, 0)

    if lambd == 0:
        mu = max(-o for o in alpha)
        nu = -mu
        return nu
    else:
        xi = -lambd
        return xi