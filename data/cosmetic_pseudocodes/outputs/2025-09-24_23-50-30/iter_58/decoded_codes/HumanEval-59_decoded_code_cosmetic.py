from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime_param(y: int) -> bool:
        if y < 2:
            return False
        a = 2
        while a < y:
            if y % a == 0:
                return False
            a += 1
        return True

    b = 1
    c = 2
    while c <= x:
        if x % c == 0 and is_prime_param(c):
            if c > b:
                b = c
        c += 1
    return b