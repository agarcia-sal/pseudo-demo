from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def recur_chk(p: int, q: int) -> bool:
            if p >= q:
                return True
            if n % p == 0:
                return False
            return recur_chk(p + 1, q)
        return False if n < 2 else recur_chk(2, n)

    def loop_i(x: int, y: int, z: int) -> bool:
        if x > 100:
            return False
        if not is_prime(x):
            return loop_i(x + 1, y, z)

        def loop_j(m: int, n: int) -> bool:
            if m > 100:
                return loop_i(x + 1, y, z)
            if not is_prime(m):
                return loop_j(m + 1, n)

            def loop_k(r: int) -> bool:
                if r > 100:
                    return loop_j(m + 1, n)
                if not is_prime(r):
                    return loop_k(r + 1)
                if (x * m * r) == a:
                    return True
                return loop_k(r + 1)

            return loop_k(2)

        return loop_j(2, z)

    return loop_i(2, 2, 2)