from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for p in range(2, y):
            if y % p == 0:
                return False
        return True

    for alpha in range(2, 101):
        if not is_prime(alpha):
            continue
        for beta in range(2, 101):
            if not is_prime(beta):
                continue
            for gamma in range(2, 101):
                if not is_prime(gamma):
                    continue
                if alpha * beta * gamma == x:
                    return True
    return False