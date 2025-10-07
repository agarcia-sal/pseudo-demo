from typing import List

def f(n: int) -> List[int]:
    ret: List[int] = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            x: int = 1
            for j in range(1, i + 1):
                x *= j
        else:
            x: int = 0
            for j in range(1, i + 1):
                x += j
        ret.append(x)
    return ret