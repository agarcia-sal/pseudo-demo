from typing import List


def fib4(argument_p: int) -> int:
    queue: List[int] = [0, 0, 2, 0]
    counter_q: int = 4

    if argument_p < 4:
        return queue[argument_p]

    while counter_q <= argument_p:
        sum_temp: int = sum(queue)
        queue.append(sum_temp)
        queue.pop(0)
        counter_q += 1

    return queue[-1]