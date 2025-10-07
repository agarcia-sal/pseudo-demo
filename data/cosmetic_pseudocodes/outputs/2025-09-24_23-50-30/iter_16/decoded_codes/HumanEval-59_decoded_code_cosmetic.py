from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False

        def check_divisor(z: int, limit: int) -> bool:
            if z > limit:
                return True
            if y % z == 0:
                return False
            return check_divisor(z + 1, limit)

        return check_divisor(2, y - 1)

    def iterate_divisors(a: int, max_candidate: int) -> int:
        if a > max_candidate:
            return max_candidate

        if (x % a == 0) and is_prime(a):
            max_candidate = a if a > max_candidate else max_candidate

        return iterate_divisors(a + 1, max_candidate)

    return iterate_divisors(2, 1)