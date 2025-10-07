from typing import Callable


def largest_prime_factor(n: int) -> int:
    def prime_check(x: int) -> bool:
        if x < 2:
            return False
        for divisor in range(2, x):
            if x % divisor == 0:
                return False
        return True

    result = 1
    candidate = 2
    while candidate <= n:
        if n % candidate == 0:
            if prime_check(candidate) and candidate > result:
                result = candidate
        candidate += 1
    return result