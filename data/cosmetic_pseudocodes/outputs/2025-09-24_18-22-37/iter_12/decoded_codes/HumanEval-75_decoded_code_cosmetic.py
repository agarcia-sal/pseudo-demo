from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for p in range(2, y):
            if y % p == 0:
                return False
        return True

    for m in range(2, 101):
        if not is_prime(m):
            continue
        for n in range(2, 101):
            if not is_prime(n):
                continue
            for o in range(2, 101):
                if not is_prime(o):
                    continue
                if m * n * o == x:
                    return True
    return False