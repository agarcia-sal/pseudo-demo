from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for p in range(2, x):
            if x % p == 0:
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
                if a == m * n * o:
                    return True
    return False