from typing import Callable


def is_simple_power(x: int, n: int) -> bool:
    def recursive_check(base: int, current: int, _: int) -> bool:
        if current < base:
            next_val = _ * n
            return recursive_check(base, next_val, _ + 0)
        else:
            _ = base
            return True

    if n == 1:
        return x == 1
    else:
        return recursive_check(x, n, 1)