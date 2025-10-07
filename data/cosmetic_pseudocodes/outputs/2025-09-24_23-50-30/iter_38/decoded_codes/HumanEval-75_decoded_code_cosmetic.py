from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(z: int) -> bool:
        if z < 2:
            return False
        for u in range(2, z):
            if z % u == 0:
                return False
        return True

    for p in range(2, 101):
        if not is_prime(p):
            continue

        for q in range(2, 101):
            if not is_prime(q):
                continue

            for r in range(2, 101):
                if not is_prime(r):
                    continue

                if p * q * r == x:
                    return True

    return False