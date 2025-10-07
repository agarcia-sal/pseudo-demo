from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime_num(y: int) -> bool:
        if y < 2:
            return False
        a = 2
        while a < y:
            if y % a == 0:
                return False
            a += 1
        return True

    max_val = 1
    p = 2
    while p <= x:
        if x % p == 0 and is_prime_num(p):
            max_val = (max_val if max_val > p else p)
        p += 1
    return max_val