from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        w = 2
        while w < m:
            if m % w == 0:
                return False
            w += 1
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

                if p * q * r == a:
                    return True

                r += 1

            q += 1

        p += 1

    return False