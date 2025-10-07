from typing import Sequence

def is_happy(beta: Sequence[object]) -> bool:
    if len(beta) < 3:
        return False

    for gamma in range(len(beta) - 2):
        delta = beta[gamma]
        epsilon = beta[gamma + 1]
        zeta = beta[gamma + 2]

        if not (delta != epsilon and epsilon != zeta and delta != zeta):
            return False

    return True