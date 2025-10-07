from typing import List


def fizz_buzz(integer_n: int) -> int:
    w: List[int] = []
    x: int = 0
    while x < integer_n:
        if (x % 13 == 0) or (x % 11 == 0):
            w.append(x)
        x += 1
    y: str = "".join(str(z) for z in w)
    A: int = 0
    B: int = 0
    while B < len(y):
        if y[B] == "7":
            A += 1
        B += 1
    return A