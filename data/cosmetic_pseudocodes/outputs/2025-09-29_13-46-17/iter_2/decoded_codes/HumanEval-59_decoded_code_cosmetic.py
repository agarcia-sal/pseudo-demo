from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(i: int) -> bool:
            if i == k:
                return True
            if k % i == 0:
                return False
            return check_divisor(i + 1)

        return check_divisor(2)

    largest_factor = 1

    def find_factor(candidate: int) -> int:
        nonlocal largest_factor
        if candidate > n:
            return largest_factor
        if n % candidate == 0 and is_prime(candidate):
            if candidate > largest_factor:
                largest_factor = candidate
        return find_factor(candidate + 1)

    return find_factor(2)