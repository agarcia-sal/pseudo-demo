from typing import List


def anti_shuffle(alpha: str) -> str:
    beta: List[str] = alpha.split(" ")
    gamma: List[str] = []
    delta: int = 0
    while delta < len(beta):
        epsilon: str = beta[delta]
        zeta: List[str] = sorted(epsilon)
        eta: str = "".join(zeta)
        gamma.append(eta)
        delta += 1
    iota: str = ""
    if len(gamma) > 0:
        iota = gamma[0]
        for kappa in range(1, len(gamma)):
            iota += " " + gamma[kappa]
    return iota