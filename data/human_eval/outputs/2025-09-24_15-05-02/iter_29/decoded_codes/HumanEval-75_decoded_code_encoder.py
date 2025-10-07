from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                return False
        return True

    if a < 8:  # smallest product of three primes (2*2*2) is 8
        return False

    primes = [i for i in range(2, 101) if is_prime(i)]

    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False