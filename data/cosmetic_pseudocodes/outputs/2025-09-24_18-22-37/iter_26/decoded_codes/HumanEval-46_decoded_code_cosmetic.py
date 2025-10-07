from collections import deque
from typing import Deque

def fib4(param_x: int) -> int:
    buffer: Deque[int] = deque([0, 0, 2, 0], maxlen=4)  # fixed size buffer for last 4 elements
    if param_x < 4:
        return buffer[param_x]

    cursor = 4
    while cursor <= param_x:
        a, b, c, d = buffer  # unpack last 4 values in order
        sum_ = a + b + c + d
        buffer.append(sum_)
        cursor += 1

    return buffer[-1]