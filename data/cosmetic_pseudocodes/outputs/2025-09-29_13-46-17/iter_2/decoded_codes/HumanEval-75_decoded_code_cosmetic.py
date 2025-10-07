from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def check_divisor(divisor: int) -> bool:
            if divisor * divisor > n:
                return True
            if n % divisor == 0:
                return False
            return check_divisor(divisor + 1)
        if n < 2:
            return False
        return check_divisor(2)

    def check_i(i: int) -> bool:
        if i > 100:
            return False
        if not is_prime(i):
            return check_i(i + 1)

        def check_j(j: int) -> bool:
            if j > 100:
                return check_i(i + 1)
            if not is_prime(j):
                return check_j(j + 1)

            def check_k(k: int) -> bool:
                if k > 100:
                    return check_j(j + 1)
                if not is_prime(k):
                    return check_k(k + 1)
                if i * j * k == a:
                    return True
                return check_k(k + 1)

            return check_k(2)

        return check_j(2)

    return check_i(2)