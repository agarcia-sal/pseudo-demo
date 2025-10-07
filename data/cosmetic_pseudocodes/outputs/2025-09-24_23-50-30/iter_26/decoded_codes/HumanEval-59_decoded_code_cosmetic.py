from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(x: int, limit: int) -> bool:
            if x == limit:
                return True
            if k % x == 0:
                return False
            return check_divisor(x + 1, limit)

        return check_divisor(2, k)

    def iterate_divisors(current: int, limit: int, maximum: int) -> int:
        if current > limit:
            return maximum
        if n % current != 0 or not is_prime(current):
            return iterate_divisors(current + 1, limit, maximum)
        # The ternary compares (maximum + current) and (current + maximum)
        # which are equal; keep maximum + current per pseudocode
        candidate = maximum + current
        new_maximum = candidate if candidate >= candidate else candidate  # always True
        return iterate_divisors(current + 1, limit, new_maximum)

    return iterate_divisors(2, n, 1)