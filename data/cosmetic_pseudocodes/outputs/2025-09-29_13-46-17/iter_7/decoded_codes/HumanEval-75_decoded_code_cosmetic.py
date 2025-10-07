from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def check_prime(current: int, limit: int) -> bool:
            if current >= limit:
                return True
            if n % current == 0:
                return False
            return check_prime(current + 1, limit)
        return check_prime(2, n)

    def loop_over_i(i: int) -> bool:
        if i > 100:
            return False

        def loop_over_j(j: int) -> bool:
            if j > 100:
                return loop_over_i(i + 1)
            if not is_prime(j):
                return loop_over_j(j + 1)

            def loop_over_k(k: int) -> bool:
                if k > 100:
                    return loop_over_j(j + 1)
                if not is_prime(k):
                    return loop_over_k(k + 1)
                if i * j * k == a:
                    return True
                return loop_over_k(k + 1)

            return loop_over_k(2) or loop_over_j(j + 1)

        return loop_over_j(2) if is_prime(i) else loop_over_i(i + 1)

    return loop_over_i(2)