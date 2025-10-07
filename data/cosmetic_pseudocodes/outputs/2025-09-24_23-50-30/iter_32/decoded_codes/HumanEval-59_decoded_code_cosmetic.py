from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y <= 1:
            return False
        for a in range(2, y):
            if y % a == 0:
                return False
        return True

    b = 1
    for c in range(2, x + 1):
        if x % c == 0 and is_prime(c):
            if b < c:
                b = c
    return b