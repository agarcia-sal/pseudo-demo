from collections import deque
from typing import Deque

def fib4(p0: int) -> int:
    p1: Deque[int] = deque([0, 0, 2, 0])
    if p0 < 4:
        return p1[p0]
    p2: int = 4
    while True:
        if p2 > p0:
            return p1[p0]
        p3, p4, p5, p6 = p1[0], p1[1], p1[2], p1[3]
        p7 = p3 + p4 + p5 + p6
        p1.append(p7)
        p1.popleft()
        p2 += 1