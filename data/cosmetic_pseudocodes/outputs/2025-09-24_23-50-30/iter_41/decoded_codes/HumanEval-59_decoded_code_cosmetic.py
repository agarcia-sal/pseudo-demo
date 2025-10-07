from typing import Callable


def largest_prime_factor(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False

        def check_divisor(gamma: int, delta: int) -> bool:
            if delta > gamma - 1:
                return True
            if gamma % delta == 0:
                return False
            return check_divisor(gamma, delta + 1)

        return check_divisor(beta, 2)

    omega: int = 1
    zeta: int = 2
    while zeta <= alpha:
        if alpha % zeta != 0:
            zeta += 1
        elif not is_prime(zeta):
            zeta += 1
        else:
            omega = omega if omega > zeta else zeta
            zeta += 1
    return omega