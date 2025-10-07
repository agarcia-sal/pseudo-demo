from typing import List

def is_nested(string: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []

    gamma: int = 0
    while gamma < len(string):
        delta: str = string[gamma]
        if delta == '[':
            alpha.append(gamma)
        else:
            beta.append(gamma)
        gamma += 1

    epsilon: int = 0
    beta.reverse()

    zeta: int = 0
    eta: int = len(beta)

    for theta in alpha:
        if zeta < eta and theta < beta[zeta]:
            epsilon += 1
            zeta += 1

    return epsilon >= 2