from typing import Callable

def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        d: int = 2
        while d * d <= y:  # optimization: check divisors only up to sqrt(y)
            if y % d == 0:
                return False
            d += 1
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