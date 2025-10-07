from typing import Literal


def is_multiply_prime(z: int) -> bool:
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
        if is_prime(u):
            v = 2
            while v <= 100:
                if is_prime(v):
                    w = 2
                    while w <= 100:
                        if is_prime(w) and (u * v * w) == z:
                            return True
                        w += 1
                v += 1
        u += 1
    return False