from typing import Callable


def is_multiply_prime(p: int) -> bool:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        m: int = 2
        while m < q:
            if q % m == 0:
                return False
            m += 1
        return True

    x: int = 2
    while x <= 100:
        if not is_prime(x):
            x += 1
            continue
        y: int = 2
        while y <= 100:
            if not is_prime(y):
                y += 1
                continue
            z: int = 2
            while z <= 100:
                if not is_prime(z):
                    z += 1
                    continue
                if p == z * y * x:
                    return True
                z += 1
            y += 1
        x += 1
    return False