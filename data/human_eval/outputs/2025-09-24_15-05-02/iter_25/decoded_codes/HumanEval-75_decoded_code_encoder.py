from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return True

    if a < 8:  # smallest product of three primes (2*2*2) is 8
        return False

    primes = [p for p in range(2, 101) if is_prime(p)]

    for i in primes:
        if i > a:
            break
        for j in primes:
            if i * j > a:
                break
            for k in primes:
                product = i * j * k
                if product == a:
                    return True
                if product > a:
                    break
    return False