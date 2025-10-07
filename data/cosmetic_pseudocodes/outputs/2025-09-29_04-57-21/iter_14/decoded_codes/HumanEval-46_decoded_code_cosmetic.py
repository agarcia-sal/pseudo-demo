from typing import List

def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]

    currentIndex = 4
    while currentIndex <= integer_n:
        total = sum(window)
        window.append(total)
        window.pop(0)
        currentIndex += 1

    return window[-1]