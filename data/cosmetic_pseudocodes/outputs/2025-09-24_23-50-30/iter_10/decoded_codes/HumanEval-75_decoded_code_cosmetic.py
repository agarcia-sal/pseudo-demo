from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        m = 2
        while m < x:
            if x % m == 0:
                return False
            m += 1
        return True

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
            s = 2
            while s <= 100:
                if not is_prime(s):
                    s += 1
                    continue
                if q * r * s == a:
                    return True
                s += 1
            r += 1
        q += 1
    return False