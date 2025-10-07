from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for idx in range(2, x):
            if x % idx == 0:
                return False
        return True

    for p in range(2, 101):
        if is_prime(p):
            for q in range(2, 101):
                if is_prime(q):
                    for r in range(2, 101):
                        if is_prime(r) and p * q * r == a:
                            return True
    return False