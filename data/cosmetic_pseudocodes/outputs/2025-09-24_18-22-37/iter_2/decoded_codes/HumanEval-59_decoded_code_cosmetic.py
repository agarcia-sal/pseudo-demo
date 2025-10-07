from typing import Callable


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

    max_prime: int = 1
    for candidate in range(2, n + 1):
        if n % candidate == 0 and is_prime(candidate):
            if candidate > max_prime:
                max_prime = candidate
    return max_prime