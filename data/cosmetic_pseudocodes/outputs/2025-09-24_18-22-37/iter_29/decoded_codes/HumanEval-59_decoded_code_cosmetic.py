from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for m in range(2, y):
            if y % m == 0:
                return False
        return True

    p: int = 1
    q: int = 2
    while q <= x:
        if x % q == 0 and is_prime(q):
            if p < q:
                p = q
        q += 1

    return p