from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        p = 2
        while p < m:
            if m % p == 0:
                return False
            p += 1
        return True

    result = 1
    candidate = 2
    while candidate <= x:
        if x % candidate == 0 and is_prime(candidate):
            if candidate > result:
                result = candidate
        candidate += 1
    return result