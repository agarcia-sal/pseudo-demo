from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for candidate in range(2, k):
            if k % candidate == 0:
                return False
        return True

    record: int = 1
    current_divisor: int = 2
    while current_divisor <= n:
        if n % current_divisor == 0 and is_prime(current_divisor):
            if record < current_divisor:
                record = current_divisor
        current_divisor += 1

    return record