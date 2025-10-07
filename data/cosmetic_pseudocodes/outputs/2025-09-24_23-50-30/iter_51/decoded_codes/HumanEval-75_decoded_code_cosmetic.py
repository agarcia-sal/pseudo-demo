from typing import Callable


def is_multiply_prime(z: int) -> bool:
    def is_prime(p: int) -> bool:
        def check_divisor(q: int) -> bool:
            if q >= p:
                return True
            if p % q == 0:
                return False
            return check_divisor(q + 1)
        return check_divisor(2)

    def scan_i(x: int) -> bool:
        if x > 100:
            return False
        if not is_prime(x):
            return scan_i(x + 1)
        return scan_j(x, 2)

    def scan_j(a1: int, y: int) -> bool:
        if y > 100:
            return scan_i(a1 + 1)
        if not is_prime(y):
            return scan_j(a1, y + 1)
        return scan_k(a1, y, 2)

    def scan_k(a2: int, b2: int, r: int) -> bool:
        if r > 100:
            return scan_j(a2, b2 + 1)
        if not is_prime(r):
            return scan_k(a2, b2, r + 1)
        if (a2 * b2 * r) == z:
            return True
        return scan_k(a2, b2, r + 1)

    return scan_i(2)