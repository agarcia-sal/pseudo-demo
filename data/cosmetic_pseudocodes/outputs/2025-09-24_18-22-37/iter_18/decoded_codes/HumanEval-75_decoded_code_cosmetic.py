from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(z: int) -> bool:
        if z < 2:
            return False
        for u in range(2, z):
            if z % u == 0:
                return False
        return True

    omega = 2
    while omega <= 100:
        if not is_prime(omega):
            omega += 1
            continue
        beta = 2
        while beta <= 100:
            if not is_prime(beta):
                beta += 1
                continue
            for gamma in range(2, 101):
                if not is_prime(gamma):
                    continue
                if omega * beta * gamma == a:
                    return True
            beta += 1
        omega += 1

    return False