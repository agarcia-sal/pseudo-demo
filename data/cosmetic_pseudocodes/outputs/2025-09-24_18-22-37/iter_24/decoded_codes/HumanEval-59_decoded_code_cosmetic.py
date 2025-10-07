from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        idx = 2
        while idx < k:
            if k % idx == 0:
                return False
            idx += 1
        return True

    max_prime: int = 1
    candidate: int = 2
    while candidate <= n:
        if n % candidate == 0 and is_prime(candidate):
            if max_prime < candidate:
                max_prime = candidate
        candidate += 1
    return max_prime