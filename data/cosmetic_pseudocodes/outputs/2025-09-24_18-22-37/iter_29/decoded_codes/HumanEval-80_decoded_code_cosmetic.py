from typing import Sequence, Any

def is_happy(zeta: Sequence[Any]) -> bool:
    if len(zeta) < 3:
        return False

    delta = 0
    epsilon = len(zeta) - 3

    while delta <= epsilon:
        alpha = zeta[delta]
        beta = zeta[delta + 1]
        gamma = zeta[delta + 2]

        if not (alpha != beta and beta != gamma and alpha != gamma):
            return False
        delta += 1

    return True