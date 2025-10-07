from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        def check_divisor(z: int) -> bool:
            if z > y - 1:
                return True
            if y % z == 0:
                return False
            return check_divisor(z + 1)

        if y < 2:
            return False
        return check_divisor(2)

    result: int = 1

    def find_factor(w: int) -> int:
        nonlocal result
        if w > x:
            return result
        if x % w == 0 and is_prime(w):
            if w > result:
                result = w
        return find_factor(w + 1)

    return find_factor(2)