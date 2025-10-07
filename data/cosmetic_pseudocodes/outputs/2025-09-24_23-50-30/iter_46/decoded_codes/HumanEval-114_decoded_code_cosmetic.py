from typing import List

def minSubArraySum(kappa: List[int]) -> int:
    def rho(mu: int, nu: int, xi: int) -> int:
        if nu == len(kappa):
            return xi
        zeta = nu
        alpha = mu + (-kappa[zeta])
        beta = xi
        if alpha < 0:
            alpha = 0
        if beta < alpha:
            beta = alpha
        return rho(alpha, zeta + 1, beta)

    delta = rho(0, 0, 0)

    if delta == 0:
        sigma = -kappa[0]
        tau = 1
        while tau < len(kappa):
            if sigma < (-kappa[tau]):
                sigma = -kappa[tau]
            tau += 1
        delta = sigma

    omega = -delta
    return omega