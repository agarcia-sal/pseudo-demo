from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        # Check divisibility from 2 to int(sqrt(n))+1 for efficiency
        limit = int(n**0.5) + 1
        return not any(n % d == 0 for d in range(2, limit))

    def search(i: int, j: int) -> bool:
        if i > 100:
            return False
        if not is_prime(i):
            return search(i + 1, 2)
        if j > 100:
            return search(i + 1, 2)
        if not is_prime(j):
            return search(i, j + 1)
        k_candidates = [k for k in range(2, 101) if is_prime(k)]
        for k in k_candidates:
            if i * j * k == a:
                return True
        return search(i, j + 1)

    return search(2, 2)