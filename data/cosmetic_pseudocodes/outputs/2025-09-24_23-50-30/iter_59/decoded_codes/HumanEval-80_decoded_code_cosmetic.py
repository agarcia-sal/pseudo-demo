from typing import Callable


def is_happy(alpha: str) -> bool:
    if not (3 <= len(alpha)):
        return False

    def Z51(Y9: int) -> bool:
        if not (Y9 <= len(alpha) - 3):
            return True
        a, b, c = alpha[Y9], alpha[Y9 + 1], alpha[Y9 + 2]
        if a == b or b == c or a == c:
            return False
        return Z51(Y9 + 1)

    return Z51(0)