from typing import List


def is_nested(text: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    gamma: int = 0
    delta: int = 0
    epsilon: int = len(text)
    zeta: int = len(beta)

    for eta in range(epsilon):
        if text[eta] == '[':
            alpha.append(eta)
        else:
            beta.append(eta)

    beta.reverse()
    zeta = len(beta)

    for theta in alpha:
        if delta < zeta and theta < beta[delta]:
            gamma += 1
            delta += 1

    return gamma >= 2