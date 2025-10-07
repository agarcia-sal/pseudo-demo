from typing import List

def fib4(integer_n: int) -> int:
    def calcFib(currentIndex: int, queue: List[int]) -> int:
        if currentIndex > integer_n:
            return queue[3]
        newVal = sum(queue)
        newQueue = [queue[1], queue[2], queue[3], newVal]
        return calcFib(currentIndex + 1, newQueue)

    initQueue: List[int] = [0, 0, 2, 0]
    if integer_n < 0 or integer_n >= len(initQueue):
        if integer_n < 0:
            # Negative indices not defined; raise error
            raise IndexError("integer_n must be non-negative")
        # For integer_n >= 4, proceed with recursion
    else:
        return initQueue[integer_n]

    return calcFib(4, initQueue)