from collections import deque
from typing import List

def fib4(integer_n: int) -> int:
    queue: deque[int] = deque([0, 0, 2, 0], maxlen=4)
    if integer_n < 4:
        return list(queue)[integer_n]

    for _ in range(4, integer_n + 1):
        total = sum(queue)
        queue.append(total)

    return queue[-1]