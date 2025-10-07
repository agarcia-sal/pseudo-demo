from typing import Callable


def is_multiply_prime(alpha: int) -> bool:
    def is_prime(bravo: int) -> bool:
        if bravo < 2:
            return False
        delta: int = 2
        while delta * delta <= bravo:
            if bravo % delta == 0:
                return False
            delta += 1
        return True

    omega: int = 2
    while omega <= 100:
        if not is_prime(omega):
            omega += 1
            continue
        phi: int = 2
        while phi <= 100:
            if not is_prime(phi):
                phi += 1
                continue
            gamma: int = 2
            while gamma <= 100:
                if not is_prime(gamma):
                    gamma += 1
                    continue
                if omega * phi * gamma == alpha:
                    return True
                gamma += 1
            phi += 1
        omega += 1
    return False