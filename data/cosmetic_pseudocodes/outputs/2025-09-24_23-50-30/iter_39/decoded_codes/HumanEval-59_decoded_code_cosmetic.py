from typing import Callable


def largest_prime_factor(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False

        def check_divisor(gamma: int) -> bool:
            if gamma >= beta:
                return True
            if beta % gamma == 0:
                return False
            return check_divisor(gamma + 1)

        return check_divisor(2)

    sigma: int = 1
    delta: int = 2

    while delta <= alpha:
        if alpha % delta == 0 and is_prime(delta):
            if sigma < delta:
                sigma = delta
        delta += 1

    return sigma