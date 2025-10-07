from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for idx in range(2, k):
            if k % idx == 0:
                return False
        return True

    max_factor: int = 1
    divisor: int = 2
    while divisor <= n:
        if n % divisor == 0:
            if is_prime(divisor):
                if divisor > max_factor:
                    max_factor = divisor
        divisor += 1
    return max_factor