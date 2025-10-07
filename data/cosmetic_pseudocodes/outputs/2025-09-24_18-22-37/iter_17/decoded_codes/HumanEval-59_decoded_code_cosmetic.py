from typing import Callable

def largest_prime_factor(n: int) -> int:
    def recall_prime(x: int) -> bool:
        if x < 2:
            return False
        current = 2
        while current < x:
            if x % current == 0:
                return False
            current += 1
        return True

    max_factor = 1
    divisor = 2
    while divisor <= n:
        if n % divisor == 0 and recall_prime(divisor):
            if divisor > max_factor:
                max_factor = divisor
        divisor += 1
    return max_factor