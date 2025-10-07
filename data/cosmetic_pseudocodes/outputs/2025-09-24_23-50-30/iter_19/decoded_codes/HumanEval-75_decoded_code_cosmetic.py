from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        idx: int = 2
        while idx < m:
            if m % idx == 0:
                return False
            idx += 1
        return True

    primes = [x for x in range(2, 101) if is_prime(x)]
    for x in primes:
        for y in primes:
            for z in primes:
                if a == x * y * z:
                    return True
    return False