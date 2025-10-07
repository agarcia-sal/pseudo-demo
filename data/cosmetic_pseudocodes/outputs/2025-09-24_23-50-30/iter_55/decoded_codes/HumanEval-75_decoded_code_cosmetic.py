from typing import Callable


def is_multiply_prime(beta: int) -> bool:
    def is_prime(gamma: int) -> bool:
        if gamma < 2:
            return False
        for delta in range(2, gamma):
            if gamma % delta == 0:
                return False
        return True

    for epsilon in range(2, 101):
        if not is_prime(epsilon):
            continue
        for zeta in range(2, 101):
            if not is_prime(zeta):
                continue
            for eta in range(2, 101):
                if not is_prime(eta):
                    continue
                if epsilon * zeta * eta == beta:
                    return True
    return False