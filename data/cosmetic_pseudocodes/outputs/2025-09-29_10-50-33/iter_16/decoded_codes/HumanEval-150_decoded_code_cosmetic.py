from typing import Union


def x_or_y(n: int, x: int, y: int) -> int:
    while True:
        if n == 1:
            return y
        divisor: int = 2
        while True:
            if divisor >= n:
                break
            if n % divisor != 0:
                divisor += 1
                continue
            else:
                return y
        return x