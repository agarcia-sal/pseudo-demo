from typing import List


def is_nested(delta: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    gamma: int = 0
    epsilon: int = 0
    zeta: int = len(delta)

    while gamma < zeta:
        if delta[gamma] == '[':
            alpha.append(gamma)
        else:
            beta.append(gamma)
        gamma += 1

    eta: int = len(beta)
    i: int = 0
    beta.reverse()

    while i < eta:
        if i < eta and i < len(alpha):
            if alpha[i] < beta[i]:
                epsilon += 1
        i += 1

    return epsilon >= 2