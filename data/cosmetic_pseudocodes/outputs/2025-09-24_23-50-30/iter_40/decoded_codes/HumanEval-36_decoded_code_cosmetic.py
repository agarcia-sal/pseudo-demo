from typing import List


def fizz_buzz(integer_n: int) -> int:
    x: List[int] = []
    for y in range(integer_n):
        if not ((y % 11) != 0 and (y % 13) != 0):
            x.append(y)
    z: str = "".join(str(w) for w in x)
    a: int = 0
    for b in z:
        a += 1 if b == "7" else 0
    return a