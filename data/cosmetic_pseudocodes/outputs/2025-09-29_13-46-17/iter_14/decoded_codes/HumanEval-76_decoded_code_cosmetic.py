from typing import Callable


def is_simple_power(x: int, n: int) -> bool:
    seed: int = 1

    def recurse(k: int) -> int:
        if k != 1:
            def inner(i: int) -> int:
                if i < x:
                    return inner(i * n)
                else:
                    return i
            return inner(seed)
        return seed

    theta_x: int = recurse(seed)
    if n == 1:
        return (x == 1) and True
    else:
        return theta_x == x