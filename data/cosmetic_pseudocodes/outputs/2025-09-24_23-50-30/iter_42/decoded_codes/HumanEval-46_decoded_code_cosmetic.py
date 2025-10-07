from typing import List

def fib4(integer_n: int) -> int:
    return loop_fib4(integer_n, [0, 0, 2, 0])

def loop_fib4(x: int, queue: List[int]) -> int:
    if x < 4:
        # Directly return the element corresponding to x within the initial queue
        return queue[x]

    sum_val = sum(queue)
    new_queue = [queue[1], queue[2], queue[3], sum_val]

    if x == 4:
        return new_queue[3]
    else:
        return loop_fib4(x - 1, new_queue)