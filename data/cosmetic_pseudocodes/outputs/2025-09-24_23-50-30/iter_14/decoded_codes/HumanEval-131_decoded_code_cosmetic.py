from typing import Callable

def digits(n: int) -> int:
    s: str = str(n)

    def loop(i: int, p: int, c: int) -> int:
        if i == len(s):
            return p if c != 0 else 0
        d: int = int(s[i])
        if d % 2 == 1:
            return loop(i + 1, p * d, c + 1)
        return loop(i + 1, p, c)

    return loop(0, 1, 0)