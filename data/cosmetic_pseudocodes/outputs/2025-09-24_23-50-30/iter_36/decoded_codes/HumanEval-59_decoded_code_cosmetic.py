from typing import Optional


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(x: int, limit: int) -> bool:
            if x == limit:
                return True
            if k % x == 0:
                return False
            return check_divisor(x + 1, limit)

        return check_divisor(2, k)

    max_factor: int = 1

    def scan_divisor(y: int) -> None:
        nonlocal max_factor
        if y > n:
            return
        if n % y == 0 and is_prime(y):
            if y > max_factor:
                max_factor = y
        scan_divisor(y + 1)

    scan_divisor(2)
    return max_factor