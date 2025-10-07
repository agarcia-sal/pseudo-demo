from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k <= 1:
            return False
        x = 2
        while x < k:
            if k % x == 0:
                return False
            x += 1
        return True

    result = 1
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            if is_prime(divisor):
                if divisor > result:
                    result = divisor
        divisor += 1
    return result