from typing import Callable


def largest_prime_factor(p: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for r in range(2, q):
            if q % r == 0:
                return False
        return True

    max_val: int = 1
    for s in range(2, p + 1):
        if p % s == 0 and is_prime(s):
            if s > max_val:
                max_val = s
    return max_val