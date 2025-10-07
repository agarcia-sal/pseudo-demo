from collections import deque
from typing import Deque


def fib4(integer_n: int) -> int:
    queue: Deque[int] = deque([0, 0, 2, 0], maxlen=4)

    if integer_n >= 4:
        index: int = 4
        while index <= integer_n:
            sum_four: int = sum(queue)  # sum all 4 elements in the queue
            queue.popleft()
            queue.append(sum_four)
            index += 1
        return queue[3]
    else:
        return queue[integer_n]