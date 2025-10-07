from typing import Any


def modp(alpha_beta: int, gamma_delta: int) -> int:
    epsilon_zeta: int = 1
    kappa_theta: int = 0
    while kappa_theta < alpha_beta:
        if kappa_theta == alpha_beta - 1:
            break
        lambda_mu: int = 2 * epsilon_zeta
        epsilon_zeta = lambda_mu % gamma_delta
        kappa_theta += 1
    return epsilon_zeta