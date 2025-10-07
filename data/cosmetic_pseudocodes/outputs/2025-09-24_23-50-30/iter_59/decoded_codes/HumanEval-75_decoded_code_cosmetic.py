from typing import Callable


def is_multiply_prime(b: int) -> bool:
    def is_prime(c: int) -> bool:
        d = 2
        while True:
            if d >= c:
                break
            if c % d == 0:
                return False
            d += 1
        return True

    e = 2
    while True:
        if e > 100:
            break
        if is_prime(e):
            f = 2
            while True:
                if f > 100:
                    break
                if is_prime(f):
                    g = 2
                    while True:
                        if g > 100:
                            break
                        if not is_prime(g):
                            g += 1
                            continue
                        if (e * f * g) == b:
                            return True
                        g += 1
                f += 1
        e += 1
    return False