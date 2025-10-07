from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for q in range(2, x):
            if x % q == 0:
                return False
        return True

    for u in range(2, 101):
        if not is_prime(u):
            continue
        for v in range(2, 101):
            if not is_prime(v):
                continue
            for w in range(2, 101):
                if not is_prime(w):
                    continue
                if a == u * v * w:
                    return True
    return False