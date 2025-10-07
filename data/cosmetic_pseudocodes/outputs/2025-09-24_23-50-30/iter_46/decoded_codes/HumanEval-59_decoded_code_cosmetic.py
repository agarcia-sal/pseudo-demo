from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False

        def check_divisor(x: int, y: int) -> bool:
            if x >= y:
                return True
            if m % x == 0:
                return False
            return check_divisor(x + 1, y)

        return check_divisor(2, m)

    def loop_over_candidates(p: int, q: int) -> int:
        if p > q:
            return 1
        if n % p == 0:
            if is_prime(p):
                return max(p, loop_over_candidates(p + 1, q))
            else:
                return loop_over_candidates(p + 1, q)
        return loop_over_candidates(p + 1, q)

    return loop_over_candidates(2, n)