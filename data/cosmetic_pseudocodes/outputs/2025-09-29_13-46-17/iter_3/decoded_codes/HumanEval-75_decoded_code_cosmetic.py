from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def check_divisor(x: int) -> bool:
            if x > n - 1:
                return True
            if n % x == 0:
                return False
            return check_divisor(x + 1)
        return check_divisor(2)

    def search_factors(x: int) -> bool:
        for p in range(2, 101):
            if is_prime(p):
                for q in range(2, 101):
                    if is_prime(q):
                        for r in range(2, 101):
                            if is_prime(r) and p * q * r == x:
                                return True
        return False

    return search_factors(a)