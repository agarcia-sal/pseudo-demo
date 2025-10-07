from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        u = 2
        while u <= x - 1:
            if x % u == 0:
                return False
            u += 1
        return True

    alpha = 2
    while alpha <= 100:
        if not is_prime(alpha):
            alpha += 1
            continue
        beta = 2
        while beta <= 100:
            if not is_prime(beta):
                beta += 1
                continue
            gamma = 2
            while gamma <= 100:
                if not is_prime(gamma):
                    gamma += 1
                    continue
                product = alpha * beta
                value_check = product * gamma
                if value_check == a:
                    return True
                gamma += 1
            beta += 1
        alpha += 1
    return False