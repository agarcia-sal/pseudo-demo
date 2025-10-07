from typing import Iterator


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k <= 1:
            return False
        divisor = 2
        while divisor < k:
            if k % divisor == 0:
                return False
            divisor += 1
        return True

    max_prime_factor = 1
    candidate = 2
    while candidate <= n:
        if n % candidate == 0 and is_prime(candidate):
            if candidate > max_prime_factor:
                max_prime_factor = candidate
        candidate += 1
    return max_prime_factor