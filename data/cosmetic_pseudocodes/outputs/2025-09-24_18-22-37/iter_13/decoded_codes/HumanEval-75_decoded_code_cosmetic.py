from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        p: int = 2
        while p <= m - 1:
            if m % p == 0:
                return False
            p += 1
        return True

    u: int = 2
    while True:
        if u > 100:
            break
        if not is_prime(u):
            u += 1
            continue

        v: int = 2
        while True:
            if v > 100:
                break
            if not is_prime(v):
                v += 1
                continue

            w: int = 2
            while True:
                if w > 100:
                    break
                if not is_prime(w):
                    w += 1
                    continue

                product: int = u * v * w
                if product == x:
                    return True

                w += 1
            v += 1
        u += 1

    return False