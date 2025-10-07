from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(current: int) -> bool:
            if current == k:
                return True
            if k % current == 0:
                return False
            return check_divisor(current + 1)

        return check_divisor(2)

    max_factor: int = 1

    def find_largest_factor(candidate: int) -> int:
        nonlocal max_factor
        if candidate > n:
            return max_factor

        if n % candidate == 0:
            if is_prime(candidate):
                if candidate > max_factor:
                    max_factor = candidate

        return find_largest_factor(candidate + 1)

    return find_largest_factor(2)