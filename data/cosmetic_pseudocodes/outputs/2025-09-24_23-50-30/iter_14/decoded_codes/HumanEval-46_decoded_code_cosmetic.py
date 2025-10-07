from typing import List

def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]

    counter: int = 4
    while counter <= integer_n:
        total: int = sum(window)
        counter += 1
        window = [window[1], window[2], window[3], total]
    return window[3]