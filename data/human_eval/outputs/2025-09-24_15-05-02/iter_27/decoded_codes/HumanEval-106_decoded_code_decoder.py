from typing import List

def f(n: int) -> List[int]:
    if n < 1:
        raise ValueError("Input must be a positive integer")

    ret: List[int] = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            # Compute factorial of i
            x: int = 1
            for j in range(1, i + 1):
                x *= j
            ret.append(x)
        else:
            # Compute sum of 1 through i
            x: int = 0
            for j in range(1, i + 1):
                x += j
            ret.append(x)
    return ret