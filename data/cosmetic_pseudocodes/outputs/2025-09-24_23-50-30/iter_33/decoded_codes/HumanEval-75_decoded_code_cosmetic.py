from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        def check_divisor(current: int, limit: int) -> bool:
            if current > limit:
                return True
            if x % current == 0:
                return False
            return check_divisor(current + 1, limit)
        return check_divisor(2, x - 1)

    def find_factors(p: int, q: int, r: int) -> bool:
        if p > 100:
            return False
        if not is_prime(p):
            return find_factors(p + 1, q, r)
        if q > 100:
            return find_factors(p + 1, 2, 2)
        if not is_prime(q):
            return find_factors(p, q + 1, r)
        if r > 100:
            return find_factors(p, q + 1, 2)
        if not is_prime(r):
            return find_factors(p, q, r + 1)
        if p * q * r == a:
            return True
        return find_factors(p, q, r + 1)

    return find_factors(2, 2, 2)