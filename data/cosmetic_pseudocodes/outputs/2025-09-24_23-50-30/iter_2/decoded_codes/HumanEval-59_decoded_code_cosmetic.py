from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        def check_divisor(d: int) -> bool:
            if d * d > k:
                return True
            if k % d == 0:
                return False
            return check_divisor(d + 1)
        if k < 2:
            return False
        return check_divisor(2)

    largest_factor: int = 1
    candidate: int = n
    while candidate >= 2:
        if n % candidate == 0:
            if is_prime(candidate):
                if candidate > largest_factor:
                    largest_factor = candidate
        candidate -= 1
    return largest_factor