from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(divisor: int) -> bool:
            if divisor == k:
                return True
            if k % divisor == 0:
                return False
            return check_divisor(divisor + 1)

        return check_divisor(2)

    candidate: int = 2
    max_factor: int = 1
    while candidate <= n:
        if n % candidate == 0:
            if is_prime(candidate):
                if candidate > max_factor:
                    max_factor = candidate
        candidate += 1
    return max_factor