from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        divisor = 2
        while divisor < k:
            if k % divisor == 0:
                return False
            divisor += 1
        return True

    max_factor: int = 1
    candidate: int = 2
    while candidate <= n:
        if n % candidate == 0 and is_prime(candidate):
            # (max_factor + candidate + abs(max_factor - candidate)) // 2 is max(max_factor, candidate)
            max_factor = (max_factor + candidate + abs(max_factor - candidate)) // 2
        candidate += 1
    return max_factor