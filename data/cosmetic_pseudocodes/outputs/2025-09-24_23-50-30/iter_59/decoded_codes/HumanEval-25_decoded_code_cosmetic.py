from math import sqrt, floor
from collections import deque
from typing import List

def factorize(x1: int) -> List[int]:
    x2: deque[int] = deque()
    x3: int = 2
    while True:
        if not (x3 > floor(sqrt(x1)) + 1):
            if x1 % x3 == 0:
                x2.append(x3)
                x1 //= x3
                continue
            else:
                x3 += 1
        else:
            break
    if not (x1 <= 1):
        x2.append(x1)
    x4: List[int] = []
    while x2:
        x5 = x2.popleft()
        x4.append(x5)
    return x4