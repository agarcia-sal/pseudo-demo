from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime_number(y: int) -> bool:
        if y < 2:
            return False
        for m in range(2, y):
            if y % m == 0:
                return False
        return True

    max_factor = 1
    divisor = 2
    while divisor <= x:
        if x % divisor == 0 and is_prime_number(divisor):
            if max_factor < divisor:
                max_factor = divisor
        divisor += 1
    return max_factor