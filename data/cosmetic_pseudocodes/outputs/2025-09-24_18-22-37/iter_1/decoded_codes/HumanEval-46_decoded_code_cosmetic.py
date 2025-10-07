from typing import List

def fib4(integer_n: int) -> int:
    queue: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return queue[integer_n]

    for _ in range(4, integer_n + 1):
        total = sum(queue)
        queue.pop(0)
        queue.append(total)

    return queue[3]