from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def test_divisor(x: int, limit: int) -> bool:
            if x > limit:
                return True
            if n % x == 0:
                return False
            return test_divisor(x + 1, limit)
        return test_divisor(2, n - 1)

    def check_triplets(i: int, j: int, k: int) -> bool:
        if i > 100:
            return False
        if not is_prime(i):
            return check_triplets(i + 1, 2, 2)
        if j > 100:
            return check_triplets(i + 1, 2, 2)
        if not is_prime(j):
            return check_triplets(i, j + 1, 2)
        if k > 100:
            return check_triplets(i, j + 1, 2)
        if not is_prime(k):
            return check_triplets(i, j, k + 1)
        if i * j * k == a:
            return True
        return check_triplets(i, j, k + 1)

    return check_triplets(2, 2, 2)