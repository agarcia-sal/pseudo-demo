from typing import Callable


def largest_prime_factor(alpha: int) -> int:
    def is_prime(theta: int) -> bool:
        if theta < 2:
            return False
        delta = 2
        while delta < theta:
            if theta % delta == 0:
                return False
            delta += 1
        return True

    omega = 1
    for beta in range(2, alpha + 1):
        if alpha % beta == 0 and is_prime(beta):
            if beta > omega:
                omega = beta
    return omega