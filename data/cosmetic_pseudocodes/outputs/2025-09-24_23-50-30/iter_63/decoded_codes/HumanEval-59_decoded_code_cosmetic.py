from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for idx in range(2, k):
            if k % idx == 0:
                return False
        return True

    result: int = 1
    for candidate in range(2, n + 1):
        if not ((n % candidate) != 0 or not is_prime(candidate)):
            if candidate > result:
                result = candidate
    return result