from typing import NoReturn


def is_multiply_prime(x: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        p = 2
        while p <= m - 1:
            if m % p == 0:
                return False
            p += 1
        return True

    r = 2
    while r <= 100:
        if not is_prime(r):
            r += 1
            continue

        s = 2
        while s <= 100:
            if not is_prime(s):
                s += 1
                continue

            t = 2
            while t <= 100:
                if not is_prime(t):
                    t += 1
                    continue

                v = r * s * t
                if v == x:
                    return True
                t += 1

            s += 1

        r += 1

    return False