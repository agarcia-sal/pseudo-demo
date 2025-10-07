from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        # Check divisibility up to sqrt(n) for efficiency
        limit = int(n**0.5) + 1
        for divisor in range(2, limit):
            if n % divisor == 0:
                return False
        return True

    if a < 8:  # Minimum product of three primes (2*2*2)
        return False

    primes = [p for p in range(2, 101) if is_prime(p)]

    # Check for any triple product equal to a
    for i in primes:
        if i > a:
            break
        for j in primes:
            if i * j > a:
                break
            for k in primes:
                product = i * j * k
                if product > a:
                    break
                if product == a:
                    return True
    return False