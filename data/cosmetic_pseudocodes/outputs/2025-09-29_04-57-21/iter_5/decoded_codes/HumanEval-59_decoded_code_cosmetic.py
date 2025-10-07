from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime_number(y: int) -> bool:
        if y < 2:
            return False
        divisor = 2
        while divisor < y:
            if y % divisor == 0:
                return False
            divisor += 1
        return True

    max_factor = 1
    candidate = 2
    while candidate <= x:
        if x % candidate == 0 and is_prime_number(candidate):
            if max_factor < candidate:
                max_factor = candidate
        candidate += 1
    return max_factor