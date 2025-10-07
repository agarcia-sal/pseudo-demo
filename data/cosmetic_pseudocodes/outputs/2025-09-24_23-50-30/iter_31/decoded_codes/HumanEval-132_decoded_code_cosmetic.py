from typing import List

def is_nested(alpha: str) -> bool:
    omega: List[int] = []
    sigma: List[int] = []
    for epsilon in range(len(alpha)):
        if alpha[epsilon] == '[':
            omega.append(epsilon)
        else:
            sigma.append(epsilon)
    sigma = [sigma[i] for i in range(len(sigma) - 1, -1, -1)]
    tau = 0
    kappa = 0
    zeta = len(sigma)
    for xi in omega:
        if kappa < zeta and xi < sigma[kappa]:
            tau += 1
            kappa += 1
    return tau >= 2