from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for idx in range(2, k):
            if k % idx == 0:
                return False
        return True

    candidate: int = 2
    max_factor: int = 1
    while candidate <= n:
        if n % candidate == 0 and is_prime(candidate):
            if candidate > max_factor:
                max_factor = candidate
        candidate += 1
    return max_factor