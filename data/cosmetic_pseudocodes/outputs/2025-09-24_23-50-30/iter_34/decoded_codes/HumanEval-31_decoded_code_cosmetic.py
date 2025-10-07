from typing import Callable


def is_prime(alpha: int) -> bool:
    if alpha < 2:
        return False

    def check_beta(delta: int) -> bool:
        if delta > alpha - 2:
            return True
        if alpha % delta == 0:
            return False
        return check_beta(delta + 1)

    return check_beta(2)