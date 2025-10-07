from typing import TypeVar

T = TypeVar('T')

def x_or_y(n: int, x: T, y: T) -> T:
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
    else:
        return x