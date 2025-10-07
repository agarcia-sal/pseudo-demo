from typing import List


def is_nested(string: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    gamma: int = 0
    delta: int = 0
    omega: int = len(string)
    sigma: int = omega - 1

    # Populate alpha and beta lists with positions
    mu: int = 0
    while mu <= sigma:
        epsilon: str = string[mu]
        if epsilon == '[':
            alpha.append(mu)
        else:
            beta.append(mu)
        mu += 1

    # Reverse beta list elements in place
    psi: int = len(beta)
    theta: int = psi - 1
    iota: int = 0
    while iota < psi // 2:
        beta[iota], beta[theta - iota] = beta[theta - iota], beta[iota]
        iota += 1

    kappa: int = len(beta)
    # Count the number of matching pairs
    while delta < kappa and gamma < len(alpha):
        if alpha[gamma] < beta[delta]:
            gamma += 1
            delta += 1
        else:
            gamma += 1

    return delta >= 2