from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime_number(y: int) -> bool:
        if y < 2:
            return False
        divisor = 2
        while divisor <= y - 1:
            if y % divisor == 0:
                return False
            divisor += 1
        return True

    max_prime_factor: int = 1
    candidate: int = 2
    while candidate <= x:
        if x % candidate == 0:
            if is_prime_number(candidate):
                max_prime_factor = (max_prime_factor if max_prime_factor > candidate else candidate)
        candidate += 1
    return max_prime_factor