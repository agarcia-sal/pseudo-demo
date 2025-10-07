from typing import List

def is_nested(zeta: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    epsilon: int = 0
    for sigma in range(len(zeta)):
        if zeta[sigma] == '[':
            alpha.append(sigma)
        else:
            beta.append(sigma)
    beta.reverse()
    delta: int = 0
    gamma: int = len(beta)
    for tau in alpha:
        if delta < gamma and tau < beta[delta]:
            epsilon += 1
            delta += 1
    omega: bool = epsilon >= 2
    return omega