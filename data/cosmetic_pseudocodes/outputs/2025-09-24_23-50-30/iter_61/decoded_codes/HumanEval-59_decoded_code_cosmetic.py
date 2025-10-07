from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for m in range(2, y):
            if y % m == 0:
                return False
        return True

    r: int = 1
    z: int = 2

    while z <= x:
        if (x % z == 0) and is_prime(z):
            if r < z:
                r = z
        z += 1

    return r