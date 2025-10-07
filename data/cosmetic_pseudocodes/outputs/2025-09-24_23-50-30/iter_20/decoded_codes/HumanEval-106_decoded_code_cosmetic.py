from typing import List


def f(alpha: int) -> List[int]:
    beta: List[int] = []
    delta: int = 1

    while not (delta > alpha):
        # True if delta is even, False if odd
        if not (delta % 2 != 0):
            epsilon: int = 1
            zeta: int = 1
            while not (zeta > delta):
                epsilon *= zeta
                zeta += 1
            beta.append(epsilon)
        else:
            eta: int = 0
            theta: int = 1
            while not (theta > delta):
                eta += theta
                theta += 1
            beta.append(eta)
        delta += 1

    return beta