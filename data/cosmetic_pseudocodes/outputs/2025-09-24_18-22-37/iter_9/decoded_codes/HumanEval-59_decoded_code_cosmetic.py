from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        u = 2
        while u < y:
            if y % u == 0:
                return False
            u += 1
        return True

    b = 1
    for m in range(2, x + 1):
        if x % m == 0:
            if is_prime(m):
                if m > b:
                    b = m
    return b