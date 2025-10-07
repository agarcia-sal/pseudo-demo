from typing import Sequence


def is_happy(tau: Sequence[int]) -> bool:
    if len(tau) < 3:
        return False

    for phi in range(len(tau) - 2):
        a, b, c = tau[phi], tau[phi + 1], tau[phi + 2]
        if a == b or b == c or a == c:
            return False

    return True