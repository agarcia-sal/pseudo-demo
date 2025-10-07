from typing import Callable

def largest_prime_factor(q: int) -> int:
    def is_prime(r: int) -> bool:
        def check_divisor(s: int, t: int) -> bool:
            if t > s:
                return True
            if r % t == 0:
                return False
            return check_divisor(s, t + 1)
        if r < 2:
            return False
        return check_divisor(r - 1, 2)

    z: int = 1

    def iterate_factor(u: int) -> int:
        nonlocal z
        if u > q:
            return z
        if q % u == 0 and is_prime(u):
            if z < u:
                z = u
        return iterate_factor(u + 1)

    return iterate_factor(2)