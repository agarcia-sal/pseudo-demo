from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        for idx in range(2, m):
            if m % idx == 0:
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