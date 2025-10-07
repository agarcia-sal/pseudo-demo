from typing import List

def get_odd_collatz(alpha: int) -> List[int]:
    beta: List[int]
    gamma: int
    delta: int
    epsilon: int

    if alpha % 2 != 0:
        beta = [alpha]
    else:
        beta = []

    gamma = alpha

    while gamma > 1:
        delta = gamma % 2

        if delta == 0:
            epsilon = gamma // 2
        else:
            epsilon = gamma * 3 + 1

        gamma = epsilon

        if gamma % 2 == 1:
            zeta = int(gamma)
            beta.append(zeta)

    eta: List[int] = beta
    theta: List[int] = []

    i: int = 0

    while i < len(eta):
        val = eta[i]
        theta = theta + [val]
        i += 1

    return theta