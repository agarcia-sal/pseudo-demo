from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        candidate = 2
        while candidate < k:
            if k % candidate == 0:
                return False
            candidate += 1
        return True

    max_prime = 1
    divisor = 2
    while divisor <= n:
        if n % divisor == 0 and is_prime(divisor):
            if max_prime < divisor:
                max_prime = divisor
        divisor += 1
    return max_prime