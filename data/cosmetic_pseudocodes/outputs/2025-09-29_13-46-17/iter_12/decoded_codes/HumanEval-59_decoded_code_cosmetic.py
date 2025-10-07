from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(x: int, y: int) -> bool:
            if y >= x:
                return True
            if x % y == 0:
                return False
            return check_divisor(x, y + 1)

        return check_divisor(k, 2)

    def search_prime(curr: int, max_factor: int) -> int:
        if curr > n:
            return max_factor
        if n % curr == 0 and is_prime(curr):
            return search_prime(curr + 1, curr if max_factor < curr else max_factor)
        return search_prime(curr + 1, max_factor)

    return search_prime(2, 1)