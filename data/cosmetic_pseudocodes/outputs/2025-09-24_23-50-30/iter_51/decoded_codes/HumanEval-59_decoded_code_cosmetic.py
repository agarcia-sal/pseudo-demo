from typing import Callable


def largest_prime_factor(q: int) -> int:
    def is_prime(r: int) -> bool:
        if r < 2:
            return False

        def prime_check_helper(s: int) -> bool:
            if s >= r:
                return True
            if r % s == 0:
                return False
            return prime_check_helper(s + 1)

        return prime_check_helper(2)

    def factor_iter(t: int, current_largest: int) -> int:
        if t > q:
            return current_largest
        new_largest = current_largest
        if q % t == 0 and is_prime(t):
            if t > current_largest:
                new_largest = t
        return factor_iter(t + 1, new_largest)

    return factor_iter(2, 1)