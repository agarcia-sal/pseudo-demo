from typing import Callable

def largest_prime_factor(p: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for x in range(2, q):
            if q % x == 0:
                return False
        return True

    max_factor: int = 1
    divisor: int = 2
    while divisor <= p:
        if p % divisor == 0 and is_prime(divisor):
            if divisor > max_factor:
                max_factor = divisor
        divisor += 1

    return max_factor