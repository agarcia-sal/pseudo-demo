from typing import Callable

def is_simple_power(x: int, n: int) -> bool:
    def check(powerVal: int) -> bool:
        if not (powerVal < x):
            return powerVal == x
        return check(powerVal * n)

    if n == 1:
        return x == 1

    return check(1)