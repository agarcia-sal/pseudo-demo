from typing import List


def fib4(integer_n: int) -> int:
    slidingWindow: List[int] = [0, 0, 2, 0]
    if not (integer_n >= 4):
        return slidingWindow[integer_n]

    currentIndex: int = 4
    while currentIndex <= integer_n:
        computedSum: int = sum(slidingWindow)
        slidingWindow.append(computedSum)
        slidingWindow.pop(0)
        currentIndex += 1

    return slidingWindow[-1]