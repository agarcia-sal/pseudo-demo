from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k <= 1:
            return False
        for divisor in range(2, int(k**0.5) + 1):
            if k % divisor == 0:
                return False
        return True

    max_prime_factor: int = 1
    for factor in range(2, n + 1):
        if n % factor == 0:
            if is_prime(factor) and factor > max_prime_factor:
                max_prime_factor = factor
    return max_prime_factor