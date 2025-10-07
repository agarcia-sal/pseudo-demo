from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        p = 2
        while p < x:
            if x % p == 0:
                return False
            p += 1
        return True

    u = 2
    while u <= 100:
        if not is_prime(u):
            u += 1
            continue
        v = 2
        while v <= 100:
            if not is_prime(v):
                v += 1
                continue
            w = 2
            while w <= 100:
                if not is_prime(w):
                    w += 1
                    continue
                if u * v * w == a:
                    return True
                w += 1
            v += 1
        u += 1
    return False