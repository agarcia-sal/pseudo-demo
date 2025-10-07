from typing import List

def fib4(integer_n: int) -> int:
    sequenceQueue: List[int] = [0, 0, 2, 0]

    def recurseFib(queue: List[int], index: int) -> int:
        if index > integer_n:
            return queue[-1]
        sumLastFour = queue[-1] + queue[-2] + queue[-3] + queue[-4]
        newQueue = queue[1:] + [sumLastFour]
        return recurseFib(newQueue, index + 1)

    if integer_n >= 4:
        return recurseFib(sequenceQueue, 4)
    return sequenceQueue[integer_n]