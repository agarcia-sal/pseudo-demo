from typing import Callable


def is_multiply_prime(p: int) -> bool:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for x in range(2, q):
            if q % x == 0:
                return False
        return True

    for idx1 in range(2, 101):
        if not is_prime(idx1):
            continue
        for idx2 in range(2, 101):
            if not is_prime(idx2):
                continue
            for idx3 in range(2, 101):
                if not is_prime(idx3):
                    continue
                if idx1 * idx2 * idx3 == p:
                    return True
    return False