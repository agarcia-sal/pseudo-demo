from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k <= 1:
            return False
        for divisor in range(2, k):
            if k % divisor == 0:
                return False
        return True

    max_factor: int = 1
    for candidate in range(2, n + 1):
        if n % candidate == 0:
            if is_prime(candidate) and candidate > max_factor:
                max_factor = candidate
    return max_factor