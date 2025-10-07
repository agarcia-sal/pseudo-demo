from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        # Check divisibility from 2 up to sqrt(n) for efficiency
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if a == i * j * k:
                    return True
    return False