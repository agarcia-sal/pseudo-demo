from typing import Callable


def largest_prime_factor(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta <= 1:
            return False
        delta = 2
        while delta < beta:
            if beta % delta == 0:
                return False
            delta += 1
        return True

    omega = 1

    def scan_factors(gamma: int) -> None:
        nonlocal omega
        if gamma > alpha:
            return
        if alpha % gamma == 0 and is_prime(gamma):
            if omega < gamma:
                omega = gamma
        scan_factors(gamma + 1)

    scan_factors(2)
    return omega