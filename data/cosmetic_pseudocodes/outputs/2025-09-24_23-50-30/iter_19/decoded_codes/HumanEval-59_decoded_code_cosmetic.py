from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k <= 1:
            return False
        m = 2
        while m < k:
            if k % m == 0:
                return False
            m += 1
        return True

    candidate = 2
    best = 1
    while candidate <= n:
        if n % candidate == 0:
            if is_prime(candidate):
                if best < candidate:
                    best = candidate
        candidate += 1
    return best