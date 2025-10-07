from typing import Callable

def is_multiply_prime(x: int) -> bool:
    def prime_check(y: int) -> bool:
        if y < 2:
            return False
        for z in range(2, y):
            if y % z == 0:
                return False
        return True

    for m in range(2, 101):
        if not prime_check(m):
            continue
        for n in range(2, 101):
            if not prime_check(n):
                continue
            for p in range(2, 101):
                if not prime_check(p):
                    continue
                if m * n * p == x:
                    return True
    return False