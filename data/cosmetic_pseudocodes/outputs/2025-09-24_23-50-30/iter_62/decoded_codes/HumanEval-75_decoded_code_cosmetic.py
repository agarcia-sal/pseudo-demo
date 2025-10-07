from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        def loop(p: int) -> bool:
            if p >= y:
                return True
            if y % p == 0:
                return False
            return loop(p + 1)
        if y < 2:
            return False
        return loop(2)

    def outer_loop(m: int) -> bool:
        if m > 100:
            return False
        if not is_prime(m):
            return outer_loop(m + 1)

        def middle_loop(n: int) -> bool:
            if n > 100:
                return outer_loop(m + 1)
            if not is_prime(n):
                return middle_loop(n + 1)

            def inner_loop(o: int) -> bool:
                if o > 100:
                    return middle_loop(n + 1)
                if not is_prime(o):
                    return inner_loop(o + 1)
                if m * n * o == x:
                    return True
                return inner_loop(o + 1)

            return inner_loop(2)

        return middle_loop(2)

    return outer_loop(2)