from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Check for factors up to sqrt(n)
        limit: int = int(n ** 0.5) + 1
        for j in range(3, limit, 2):
            if n % j == 0:
                return False
        return True

    if a < 8:  # Minimum product of three primes (2*2*2=8)
        return False

    # Precompute primes up to 100 for efficiency
    primes: list[int] = [x for x in range(2, 101) if is_prime(x)]

    # Check for triples i,j,k in primes such that i*j*k == a
    for i in primes:
        if i > a:
            continue
        for j in primes:
            if i * j > a:
                continue
            if a % (i * j) != 0:
                continue
            k = a // (i * j)
            if k < 2 or k > 100:
                continue
            if k in primes:
                return True
    return False