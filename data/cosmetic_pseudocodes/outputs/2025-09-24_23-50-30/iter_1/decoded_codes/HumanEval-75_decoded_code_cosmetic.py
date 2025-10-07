from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        divisor = 2
        while divisor < n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    i = 2
    while i <= 100:
        if not is_prime(i):
            i += 1
            continue
        j = 2
        while j <= 100:
            if not is_prime(j):
                j += 1
                continue
            k = 2
            while k <= 100:
                if not is_prime(k):
                    k += 1
                    continue
                if a == i * j * k:
                    return True
                k += 1
            j += 1
        i += 1
    return False