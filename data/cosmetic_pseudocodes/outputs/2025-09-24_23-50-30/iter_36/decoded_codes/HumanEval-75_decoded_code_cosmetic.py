from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        def check_divisor(y: int) -> bool:
            if y >= x:
                return True
            if x % y == 0:
                return False
            return check_divisor(y + 1)
        return check_divisor(2)

    def scan_c(m: int) -> bool:
        if m > 100:
            return False
        if not is_prime(m):
            return scan_c(m + 1)
        return scan_b(2, m)

    def scan_b(n: int, c: int) -> bool:
        if n > 100:
            return scan_c(c + 1)
        if not is_prime(n):
            return scan_b(n + 1, c)
        return scan_a(2, n, c)

    def scan_a(p: int, n: int, c: int) -> bool:
        if p > 100:
            return scan_b(n + 1, c)
        if not is_prime(p):
            return scan_a(p + 1, n, c)
        if c * n * p == a:
            return True
        return scan_a(p + 1, n, c)

    return scan_c(2)