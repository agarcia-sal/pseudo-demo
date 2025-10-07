from typing import List


def f(beta: int) -> List[int]:
    alpha: List[int] = []
    gamma: int = 1
    delta: int = 1
    while delta <= beta:
        if delta % 2 == 0:
            gamma = 1
            epsilon = 1
            while epsilon <= delta:
                gamma *= epsilon
                epsilon += 1
            alpha.append(gamma)
        else:
            zeta = 0
            eta = 1
            while eta <= delta:
                zeta += eta
                eta += 1
            alpha.append(zeta)
        delta += 1
    return alpha