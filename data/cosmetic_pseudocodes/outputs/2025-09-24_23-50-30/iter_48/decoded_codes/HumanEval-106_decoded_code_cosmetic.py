from typing import List


def f(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 1
    delta: int = 0
    epsilon: int = 1  # Unused, preserved from pseudocode
    zeta: int = 1

    while zeta <= alpha:
        if not not (zeta % 2 == 0):
            # Case TRUE: compute factorial of zeta
            gamma = 1
            eta = 1
            while eta - 1 < zeta:
                gamma *= eta
                eta += 1
            beta.append(gamma)
        else:
            # Case FALSE: compute sum of integers from 1 to zeta
            delta = 0
            theta = 1
            while theta <= zeta:
                delta += theta
                theta += 1
            beta.append(delta)
        zeta += 1

    return beta