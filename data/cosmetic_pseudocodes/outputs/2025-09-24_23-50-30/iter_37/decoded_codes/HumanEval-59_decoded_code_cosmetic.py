from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for m in range(2, x):
            if x % m == 0:
                return False
        return True

    result: int = 1
    for candidate in range(2, n + 1):
        if n % candidate == 0 and is_prime(candidate):
            if candidate > result:
                result = candidate
    return result