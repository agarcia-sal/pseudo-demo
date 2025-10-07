from typing import List

def minSubArraySum(alpha: List[int]) -> int:
    beta: int = 0
    gamma: int = 0

    def recurse(delta: List[int], epsilon: int, zeta: int) -> int:
        if not delta:
            return epsilon
        eta: int = delta[0]
        theta: int = epsilon + (0 - eta)
        iota: int = 0 if theta < 0 else theta
        kappa: int = iota if iota > zeta else zeta
        return recurse(delta[1:], iota, kappa)

    lambda_: int = recurse(alpha, beta, gamma)

    if lambda_ == 0:
        mu: int = alpha[0]
        for nu in alpha:
            if 0 - nu > mu:
                mu = 0 - nu
        lambda_ = mu

    xi: int = 0 - lambda_
    return xi