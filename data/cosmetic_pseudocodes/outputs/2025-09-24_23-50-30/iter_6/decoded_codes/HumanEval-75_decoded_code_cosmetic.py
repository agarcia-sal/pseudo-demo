from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        x: int = 2
        while x < n:
            if n % x == 0:
                return False
            x += 1
        return True

    p: int = 2
    while p < 101:
        if not is_prime(p):
            p += 1
            continue
        q: int = 2
        while q < 101:
            if not is_prime(q):
                q += 1
                continue
            r: int = 2
            while r < 101:
                if not is_prime(r):
                    r += 1
                    continue
                if p * q * r == a:
                    return True
                r += 1
            q += 1
        p += 1
    return False