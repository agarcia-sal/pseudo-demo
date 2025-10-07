from collections import deque
from typing import Deque

def fib4(integer_n: int) -> int:
    interim_queue: Deque[int] = deque([0, 0, 2, 0], maxlen=4)
    if integer_n < 4:
        return interim_queue[integer_n]
    idx = 4
    while idx <= integer_n:
        total_sum = sum(interim_queue)
        interim_queue.append(total_sum)  # Automatically pops leftmost due to maxlen=4
        idx += 1
    return interim_queue[3]