from typing import List

def is_nested(alpha: str) -> bool:
    beta: List[int] = []
    gamma: List[int] = []
    delta: int = 0
    epsilon: int = 0
    mu: int = len(alpha)

    while epsilon < mu:
        if alpha[epsilon] == '[':
            beta.append(epsilon)
        else:
            gamma.append(epsilon)
        epsilon += 1

    # Reverse gamma
    gamma = [gamma[len(gamma) - zeta - 1] for zeta in range(len(gamma))]

    eta: int = len(gamma)
    epsilon = 0
    for theta in beta:
        if (epsilon < eta) and (theta < gamma[epsilon]):
            delta += 1
            epsilon += 1

    return not (delta < 2)