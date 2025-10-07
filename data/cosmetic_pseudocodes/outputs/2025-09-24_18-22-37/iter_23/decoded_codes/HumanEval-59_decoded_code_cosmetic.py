from typing import Callable

def largest_prime_factor(p: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for m in range(2, q):
            if q % m == 0:
                return False
        return True

    max_factor: int = 1
    r: int = 2
    while r <= p:
        if p % r == 0:
            if is_prime(r):
                if max_factor < r:
                    max_factor = r
        r += 1

    return max_factor