from typing import Callable


def is_multiply_prime(u: int) -> bool:
    def is_prime(z: int) -> bool:
        if z < 2:
            return False
        x = 2
        while x <= z - 1:
            if z % x == 0:
                return False
            x += 1
        return True

    p = 2
    while p <= 100:
        if not is_prime(p):
            p += 1
            continue

        q = 2
        while q <= 100:
            if not is_prime(q):
                q += 1
                continue

            r = 2
            while r <= 100:
                if not is_prime(r):
                    r += 1
                    continue

                t = p * q * r

                if t == u:
                    return True
                r += 1
            q += 1
        p += 1

    return False