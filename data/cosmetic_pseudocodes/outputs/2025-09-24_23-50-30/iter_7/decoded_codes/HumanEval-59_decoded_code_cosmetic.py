from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k > 1:
            def check_div(d: int) -> bool:
                if d >= k:
                    return True
                if k % d == 0:
                    return False
                return check_div(d + 1)
            return check_div(2)
        return False

    m: int = 1
    x: int = 2
    while x <= n:
        if n % x == 0:
            if is_prime(x):
                if x > m:
                    m = x
        x += 1
    return m