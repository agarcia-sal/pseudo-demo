from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        m = 2
        while m < y:
            if y % m == 0:
                return False
            m += 1
        return True

    max_factor = 1
    current = 2
    while current <= x:
        if x % current == 0 and is_prime(current):
            if current > max_factor:
                max_factor = current
        current += 1
    return max_factor