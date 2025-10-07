from typing import List, Optional


def search(z: List[int]) -> int:
    a: List[int] = [0] * (max(z) + 1)

    def f(i: int) -> None:
        if i == len(z):
            return
        a[z[i]] += 1
        f(i + 1)

    f(0)

    b: int = -1
    j: int = 1
    while j < len(a):
        if a[j] >= j:
            b = j
        j += 1

    return b