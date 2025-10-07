from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        limit = int(n**0.5) + 1
        for divisor in range(3, limit, 2):
            if n % divisor == 0:
                return False
        return True

    primes = [p for p in range(2, 101) if is_prime(p)]
    prime_set = set(primes)

    # Iterate over all prime triples whose product is a
    for i in primes:
        if i > a:
            break
        for j in primes:
            if i * j > a:
                break
            if a % (i * j) != 0:
                continue
            k = a // (i * j)
            if k in prime_set:
                return True
    return False