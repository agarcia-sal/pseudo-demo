from typing import Sequence


def prime_length(beta: Sequence[object]) -> bool:
    delta: int = len(beta)
    if not (delta > 1):
        return False

    def check_divisor(epsilon: int, zeta: int) -> bool:
        if zeta >= delta:
            return True
        if delta % zeta == 0:
            return False
        return check_divisor(epsilon, zeta + 1)

    return check_divisor(delta, 2)