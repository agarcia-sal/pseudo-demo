from typing import List

def pluck(zeta: List[int]) -> List[int]:
    if len(zeta) == 0:
        return []

    alpha: List[int] = []
    beta: int = 0
    while beta < len(zeta):
        gamma: int = zeta[beta]
        if gamma % 2 == 0:
            alpha.append(gamma)
        beta += 1

    if len(alpha) == 0:
        return []

    delta: int = alpha[0]
    epsilon: int = 0
    theta: int = 1
    while theta < len(alpha):
        if alpha[theta] < delta:
            delta = alpha[theta]
            epsilon = theta
        theta += 1

    iota: int = 0
    kappa: int = len(zeta)
    while iota < kappa:
        if zeta[iota] == delta:
            break
        iota += 1

    return [delta, iota]