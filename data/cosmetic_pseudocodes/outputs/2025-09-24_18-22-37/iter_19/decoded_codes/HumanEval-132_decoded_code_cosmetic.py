from typing import List


def is_nested(string: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    gamma: int = len(string)
    delta: int = 0
    while delta <= gamma - 1:
        if string[delta] == '[':
            alpha.append(delta)
        else:
            beta.append(delta)
        delta += 1
    beta.reverse()
    zeta: int = 0
    eta: int = 0
    epsilon: int = len(beta)
    for theta in alpha:
        if zeta < epsilon and theta < beta[zeta]:
            zeta += 1
            eta += 1
    return eta >= 2