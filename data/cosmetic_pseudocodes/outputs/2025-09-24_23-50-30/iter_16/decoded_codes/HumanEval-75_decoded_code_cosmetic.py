from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for idx in range(2, n):
            if n % idx == 0:
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
                if a == alpha * beta * gamma:
                    return True
    return False