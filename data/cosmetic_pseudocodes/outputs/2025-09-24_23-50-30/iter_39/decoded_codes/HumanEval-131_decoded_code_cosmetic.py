from typing import Tuple


def digits(x: int) -> int:
    alpha: int = 1
    beta: int = 0
    gamma: int = 0
    x_str: str = str(x)
    length: int = len(x_str)

    while gamma < length:
        delta: int = int(x_str[gamma])
        if delta % 2 == 1:
            alpha *= delta
            beta += 1
        gamma += 1

    return 0 if beta == 0 else alpha