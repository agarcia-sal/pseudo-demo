from typing import Sequence


def is_happy(zeta: Sequence[str]) -> bool:
    epsilon: int = len(zeta)
    if epsilon < 3:
        return False

    theta: int = 0
    while theta <= epsilon - 3:
        alpha: str = zeta[theta]
        beta: str = zeta[theta + 1]
        gamma: str = zeta[theta + 2]

        if alpha == beta or beta == gamma or alpha == gamma:
            return False

        theta += 1

    return True