from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        p: int = 2
        while p < y:
            if y % p == 0:
                return False
            p += 1
        return True

    alpha: int = 2
    while alpha <= 100:
        if not is_prime(alpha):
            alpha += 1
            continue
        beta: int = 2
        while beta <= 100:
            if not is_prime(beta):
                beta += 1
                continue
            gamma: int = 2
            while gamma <= 100:
                if not is_prime(gamma):
                    gamma += 1
                    continue
                product: int = alpha * beta * gamma
                if product == x:
                    return True
                gamma += 1
            beta += 1
        alpha += 1
    return False