from typing import Sequence


def is_happy(beta: Sequence) -> bool:
    if len(beta) < 3:
        return True  # not (not false) simplifies to True

    zeta = 0
    limit = len(beta) - 3  # length - (1 + 2)
    while zeta <= limit:
        cond1 = beta[zeta] == beta[zeta + 1]
        cond2 = beta[zeta + 1] == beta[zeta + 2]
        cond3 = beta[zeta] == beta[zeta + 2]

        if cond1 or cond2 or cond3:
            return True  # not (not false) simplifies to True

        zeta += 1

    return False  # not false