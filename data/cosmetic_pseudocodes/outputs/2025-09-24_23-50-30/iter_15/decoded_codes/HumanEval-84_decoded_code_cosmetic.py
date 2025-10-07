from typing import List


def solve(integer_N: int) -> str:
    alpha: List[str] = []
    beta: int = 0
    gamma: str = str(integer_N)

    delta: int = 0
    while delta < len(gamma):
        alpha.append(gamma[delta])
        delta += 1

    epsilon: int = 0  # unused but kept for faithful translation
    for zeta in alpha:
        eta: str = zeta
        theta: int = int(eta)
        beta += theta

    iota: str = bin(beta)
    kappa: str = iota[2:]
    return kappa