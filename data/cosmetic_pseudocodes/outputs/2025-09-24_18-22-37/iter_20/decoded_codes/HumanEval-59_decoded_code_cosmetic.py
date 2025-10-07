from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for q in range(2, k):
            if k % q == 0:
                return False
        return True

    max_factor: int = 1
    divisor: int = 2

    while divisor <= n:
        if n % divisor == 0 and is_prime(divisor):
            if max_factor < divisor:
                max_factor = divisor
        divisor += 1

    return max_factor