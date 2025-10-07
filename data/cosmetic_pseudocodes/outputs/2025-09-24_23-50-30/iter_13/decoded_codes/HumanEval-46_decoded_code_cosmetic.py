from collections import deque
from typing import Deque

def fib4(integer_n: int) -> int:
    buffer: Deque[int] = deque([0, 0, 2, 0], maxlen=4)
    if integer_n < 4:
        return buffer[integer_n]

    for _ in range(4, integer_n + 1):
        total = sum(buffer)
        buffer.append(total)  # automatically evicts oldest due to maxlen
    return buffer[-1]