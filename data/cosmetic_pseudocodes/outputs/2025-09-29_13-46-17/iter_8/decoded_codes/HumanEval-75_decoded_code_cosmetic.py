from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def recur_check(d: int) -> bool:
            if d == n:
                return True
            if n % d == 0:
                return False
            return recur_check(d + 1)
        return recur_check(2)

    def traverse_i(x: int) -> bool:
        if x > 100:
            return False
        if not is_prime(x):
            return traverse_i(x + 1)

        def traverse_j(y: int) -> bool:
            if y > 100:
                return traverse_i(x + 1)
            if not is_prime(y):
                return traverse_j(y + 1)

            def traverse_k(z: int) -> bool:
                if z > 100:
                    return traverse_j(y + 1)
                if not is_prime(z):
                    return traverse_k(z + 1)
                if x * y * z == a:
                    return True
                return traverse_k(z + 1)

            return traverse_k(2)

        return traverse_j(2)

    return traverse_i(2)