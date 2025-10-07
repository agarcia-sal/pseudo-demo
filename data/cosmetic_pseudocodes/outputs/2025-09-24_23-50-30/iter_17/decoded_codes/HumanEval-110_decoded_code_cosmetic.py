from typing import Sequence

def exchange(list_one: Sequence[int], list_two: Sequence[int]) -> str:
    x: int = 0
    y: int = 0
    a = list_one
    b = list_two
    for i in range(len(a)):
        if (a[i] % 2) - 1 == 0:
            x += 1
    for j in range(len(b)):
        if (b[j] % 2) - 0 == 0:
            y += 1
    if y >= x:
        return "YES"
    else:
        return "NO"