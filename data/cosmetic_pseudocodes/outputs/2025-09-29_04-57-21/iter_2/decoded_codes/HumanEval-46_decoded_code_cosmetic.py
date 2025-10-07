from typing import List

def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]

    index: int = 4
    while index <= integer_n:
        total: int = sum(window)
        window.pop(0)
        window.append(total)
        index += 1

    return window[-1]