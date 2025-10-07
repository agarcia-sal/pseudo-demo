from typing import Callable


def largest_prime_factor(a: int) -> int:
    def is_prime(b: int) -> bool:
        if b < 2:
            return False

        def check_divisor(c: int, d: int) -> None:
            nonlocal result
            if c >= d:
                result = True
            else:
                if (b % c) == 0:
                    result = False
                else:
                    check_divisor(c + 1, d)

        result: bool = False
        check_divisor(2, b)
        return result

    def loop_divisors(e: int, f: int, g: int) -> int:
        if e > f:
            return g
        if (a % e == 0) and is_prime(e):
            j = e if e > g else g
            return loop_divisors(e + 1, f, j)
        return loop_divisors(e + 1, f, g)

    return loop_divisors(2, a, 1)