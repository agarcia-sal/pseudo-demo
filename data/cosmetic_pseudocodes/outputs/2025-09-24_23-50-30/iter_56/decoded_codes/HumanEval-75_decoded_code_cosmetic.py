from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(m: int) -> bool:
        def check_divisor(p: int, q: int) -> bool:
            if q >= p:
                return True
            return (m % q != 0) and check_divisor(p, q + 1)
        return check_divisor(m, 2)

    def search_triplet(x: int, y: int, z: int) -> bool:
        if z > 100:
            return False
        if not is_prime(z):
            return search_triplet(x, y, z + 1)
        if x * y * z == a:
            return True
        return search_triplet(x, y, z + 1)

    def search_j(x: int, y: int) -> bool:
        if y > 100:
            return False
        if not is_prime(y):
            return search_j(x, y + 1)
        return search_triplet(x, y, 2) or search_j(x, y + 1)

    def search_i(x: int) -> bool:
        if x > 100:
            return False
        if not is_prime(x):
            return search_i(x + 1)
        return search_j(x, 2) or search_i(x + 1)

    return search_i(2)