from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        def F(v: int, C: int) -> bool:
            if v < 2:
                return False
            if C > v - 1:
                return True
            if v % C == 0:
                return False
            return F(v, C + 1)
        return F(k, 2)

    def G(x: int, Y: int, Z: int) -> int:
        if x > n:
            return Z
        if n % x == 0 and is_prime(x):
            return G(x + 1, Y, Z if Z > x else x)
        else:
            return G(x + 1, Y, Z)

    return G(2, 0, 1)