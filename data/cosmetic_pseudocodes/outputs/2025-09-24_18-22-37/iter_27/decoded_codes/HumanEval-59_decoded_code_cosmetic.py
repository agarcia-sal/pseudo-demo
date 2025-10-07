from typing import Callable


def largest_prime_factor(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False
        # Check divisibility from 2 up to beta-1
        delta: int = 2
        while delta <= beta - 1:
            if beta % delta == 0:
                return False
            delta += 1
        return True

    zeta: int = 1
    eta: int = 2
    while eta <= alpha:
        if alpha % eta == 0 and is_prime(eta):
            if zeta < eta:
                zeta = eta
        eta += 1
    return zeta