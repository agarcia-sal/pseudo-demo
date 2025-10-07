from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Check divisibility up to sqrt(n)
        limit = int(n**0.5) + 1
        for divisor in range(3, limit, 2):
            if n % divisor == 0:
                return False
        return True

    if a < 8:  # Smallest product of three primes (2*2*2) = 8
        return False

    # Precompute primes in [2..100] to avoid repeated checks
    primes = [num for num in range(2, 101) if is_prime(num)]

    for i in primes:
        for j in primes:
            # Early pruning: if i*j > a, skip k loop
            if i * j > a:
                continue
            for k in primes:
                product = i * j * k
                if product == a:
                    return True
                # If product exceeds a, no need to continue increasing k
                if product > a:
                    break
    return False