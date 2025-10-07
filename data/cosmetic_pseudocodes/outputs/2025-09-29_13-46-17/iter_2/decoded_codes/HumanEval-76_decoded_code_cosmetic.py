from typing import Union


def is_simple_power(x: int, n: int) -> bool:
    return (n == 1 and x == 1) or check_power(1, x, n)


def check_power(current: int, target: int, base: int) -> bool:
    if current >= target:
        return current == target
    else:
        return check_power(current * base, target, base)