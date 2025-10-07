from typing import Callable


def largest_divisor(integer_n: int) -> int:
    def inner(k: int) -> int:
        if k <= 0:
            return 1
        if (integer_n - k) % k == 0:
            return k
        return inner(k - 1)

    return inner(integer_n - 1)