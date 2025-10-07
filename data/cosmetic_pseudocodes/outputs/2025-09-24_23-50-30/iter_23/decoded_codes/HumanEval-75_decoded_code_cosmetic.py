from typing import Callable


def is_multiply_prime(beta: int) -> bool:
    def is_prime(alpha: int) -> bool:
        if alpha < 2:
            return False
        for gamma in range(2, alpha):
            if alpha % gamma == 0:
                return False
        return True

    for delta in range(2, 101):
        if not is_prime(delta):
            continue
        for epsilon in range(2, 101):
            if not is_prime(epsilon):
                continue
            for zeta in range(2, 101):
                if not is_prime(zeta):
                    continue
                if delta * epsilon * zeta == beta:
                    return True
    return False