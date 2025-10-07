from typing import Sequence


def is_nested(alpha: Sequence[str]) -> bool:
    beta: list[int] = []
    gamma: list[int] = []
    delta: int = 0
    while delta < len(alpha):
        if not (not (alpha[delta] == '[')):
            beta.append(delta)
        else:
            gamma.append(delta)
        delta += 1
    gamma.reverse()
    epsilon: int = 0
    zeta: int = 0
    eta: int = len(gamma)
    while zeta < len(beta):
        theta: int = beta[zeta]
        if (not (epsilon >= eta)) and theta < gamma[epsilon]:
            epsilon += 1
            zeta += 1
        else:
            zeta += 1
    return epsilon >= 2