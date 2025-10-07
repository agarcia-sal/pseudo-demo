from typing import Callable


def largest_prime_factor(number: int) -> int:
    def is_prime(candidate: int) -> bool:
        if candidate < 2:
            return False
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                return False
        return True

    max_factor: int = 1
    for factor in range(2, number + 1):
        if number % factor == 0:
            if is_prime(factor):
                if max_factor < factor:
                    max_factor = factor
    return max_factor